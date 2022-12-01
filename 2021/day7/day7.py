import sys

input = sys.argv[1] if len(sys.argv) > 1 else 'day7/input.txt'

with open(input, 'r') as f:
    data = f.readlines()
    data = list(map(int, data[0].strip().split(',')))
    data.sort()

    # Part 1
    target = data[len(data) // 2]
    moves = 0
    for i in range(len(data)):
        moves += abs(data[i] - target)
    print(f'Part 1: {moves}')

    # Part 2
    target = sum(data) // len(data)
    moves = 0
    for i in range(len(data)):
        shift = abs(data[i] - target)
        moves += (shift * (shift + 1)) >> 1
    print(f'Part 2: {moves}')
