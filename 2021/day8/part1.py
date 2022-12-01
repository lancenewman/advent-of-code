import sys
input = sys.argv[1] if len(sys.argv) > 1 else 'day8/input.txt'


with open(input, 'r') as f:
    lines = [tuple(line.strip().split('|')) for line in f.readlines()]
    signals = dict(lines)

    # part 1
    uniqueNums = {1: 2, 4: 4, 7: 3, 8: 7}
    easyNums = 0
    for output in signals.values():
        nums = output.strip().split()
        easyNums += len([num for num in nums if len(num)
                        in uniqueNums.values()])
    print(f'Part 1: {easyNums}')
