import sys
from typing import List
from BingoBoard import BingoBoard

if len(sys.argv) < 2:
    print('Usage: python3 day4.py input-file')
    exit()


def main() -> None:
    with open(sys.argv[1], 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        numbers = [int(num) for num in lines[0].split(',')]
        lines = lines[2:]

        boards = list()
        currentBoard = list()
        currentRow = list()
        for line in lines:
            if line:
                currentRow = [int(num) for num in line.split()]
                currentBoard.append(currentRow)

            if len(currentBoard) == BingoBoard.BOARD_SIZE:
                boards.append(BingoBoard(currentBoard))
                currentBoard = list()
        
        print(f'Part 1: {getBestWinningScore(numbers, boards)}')

        for board in boards:
            board.reset()

        print(f'Part 2: {getWorstWinningScore(numbers, boards)}')
        

# Part 1
def getBestWinningScore(numbers: int, boards: List[BingoBoard]) -> int:
    bestWinIndex = len(numbers)
    winningBoard = None
    for board in boards:
        winnerIndex = board.getWinningNumberIndex(numbers)
        if winnerIndex < bestWinIndex:
            winningBoard = board
            bestWinIndex = winnerIndex
    
    if winningBoard:
        return winningBoard.getUnmarkedSum() *  numbers[bestWinIndex]
    
    return -1

# Part 2
def getWorstWinningScore(numbers: int, boards: List[BingoBoard]) -> int:
    worstWinIndex = 0
    worstWinningBoard = None
    for board in boards:
        winnerIndex = board.getWinningNumberIndex(numbers)
        if winnerIndex > worstWinIndex:
            worstWinIndex = winnerIndex
            worstWinningBoard = board

    if worstWinningBoard:
        return worstWinningBoard.getUnmarkedSum() * numbers[worstWinIndex]

    return -1

    
if __name__ == '__main__':
    main()