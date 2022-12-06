from typing import Tuple


def evaluate_round_part_1(elf_move: str, my_move: str) -> int:
    lose_conditions = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    draw_conditions = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }

    move_values = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    my_score = move_values[my_move]

    if lose_conditions[elf_move] == my_move:
        return my_score
    elif draw_conditions[elf_move] == my_move:
        return my_score + 3
    else:
        return my_score + 6

def evaluate_round_part_2(elf_move: str, outcome: str) -> int:
    LOSE = "X"
    DRAW = "Y"

    move_values = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    win_map = {
        "A": move_values["B"],
        "B": move_values["C"],
        "C": move_values["A"]
    }

    lose_map = {
        "A": move_values["C"],
        "B": move_values["A"],
        "C": move_values["B"]
    }

    if outcome == LOSE:
        return lose_map[elf_move]
    elif outcome == DRAW:
        return move_values[elf_move] + 3
    else:
        return win_map[elf_move] + 6

def solve(file: str) -> Tuple[int,int]:
    part_1_score = 0
    part_2_score = 0
    with open(file) as input:
        for line in input:
            elf_score, my_score = line.split()
            part_1_score = part_1_score + evaluate_round_part_1(elf_score, my_score)
            part_2_score = part_2_score + evaluate_round_part_2(elf_score, my_score)
    return (part_1_score, part_2_score)


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')