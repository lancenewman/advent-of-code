import sys

from Fathometer import Fathometer

if len(sys.argv) < 2:
    print('Usage: python3 day1.py input-file')
    exit()

with open(sys.argv[1], 'r') as f:
    input = [int(line.rstrip()) for line in f]
    fathometer = Fathometer(input)
    print(f'Part 1: {fathometer.countIncreases()}')
    print(f'Part 2: {fathometer.countSlidingWindowIncreases(3)}')
