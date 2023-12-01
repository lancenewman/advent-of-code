from typing import Dict, Tuple


UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


def count_positions_visited(moves: Dict[str,int]) -> int:
    return 0


def parse_movements(filename: str) -> Dict[str,int]:
    instructions = {}
    with open(filename, 'r') as input_file:
        for line in input_file.readlines():
            direction, amount = line.strip().split()
            instructions[direction] = int(amount)
    return instructions


def solve(filename: str) -> Tuple[int,None]:
    moves = parse_movements(filename)
    positions_visited = count_positions_visited(moves)
    return (positions_visited, None)


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')