from typing import List, Tuple


class BingoBoard:
    BOARD_SIZE = 5

    def __init__(self, board: List[List[int]]) -> None:
        self.board = list()
        self.winDraws = None
        self._initBoardData(board)

    def _initBoardData(self, board: List[List[int]]) -> List[List[Tuple[int, bool]]]:
        for row in board:
            currentRow = list()
            for num in row:
                currentRow.append((num, False))
            self.board.append(currentRow)

    def reset(self) -> None:
        for row in self.board:
            for i, pair in enumerate(row):
                row[i] = (pair[0], False)

    
    def printBoard(self) -> None:
        for row in self.board:
            print([pair[0] for pair in row])
    
    def getWinningNumberIndex(self, numsDrawn: List[int]) -> int:
        """Marks the board until a win is achieved and returns the index of the winning number.
        
        Args:
            numsDrawn: A list of integers representing the order of bingo numbers drawn.
        Returns:
            The index of the winning number if a win is possible, else -1
        """
        for i, num in enumerate(numsDrawn):
            for row in self.board:
                for j, pair in enumerate(row):
                    if pair[0] == num:
                        row[j] = (pair[0], True)
            if self.isWinner():
                return i
        return -1
    
    def isWinner(self):
        return self._rowWinner() or self._columnWinner()

    def _rowWinner(self) -> bool:
        """Checks if any entire row in the board is marked.
        
        Returns:
            True if an entire row is marked, False otherwise.
        """
        for row in self.board:
            if all([pair[1] for pair in row]):
                return True
        return False
    
    def _columnWinner(self) -> bool:
        """Checks if any entire column in the board is marked.
        
        Returns:
            True if an entire column is marked, False otherwise.
        """
        for i in range(self.BOARD_SIZE):
            if all(row[i][1] for row in self.board):
                return True
        return False

    def getUnmarkedSum(self) -> int:
        sum = 0
        for row in self.board:
            for pair in row:
                if not pair[1]:
                    sum += pair[0]
        return sum