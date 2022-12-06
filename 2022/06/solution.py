from typing import Tuple

def is_unique(string: str) -> bool:
    return len(set(string)) == len(string)


def find_start_of_unique_sequence_in_signal(signal, window_size):
    for i in range(len(signal) - window_size + 1):
        if is_unique(signal[i:i+window_size]):
            return i + window_size


def find_start_of_message(signal: str) -> int:
    return find_start_of_unique_sequence_in_signal(signal, 14)


def find_start_of_packet(signal: str) -> int:
    return find_start_of_unique_sequence_in_signal(signal, 4)
        

def solve(file: str) -> Tuple[int,None]:
    with open(file, 'r') as input:
        signal = input.read()

    return (find_start_of_packet(signal), find_start_of_message(signal))


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')