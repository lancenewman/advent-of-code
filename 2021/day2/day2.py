import sys

from Submarine import Submarine

if len(sys.argv) < 2:
    print('Usage: python3 day2.py input-file')
    exit()

with open(sys.argv[1], 'r') as f:
    input = [line.rstrip() for line in f]
    submarine = Submarine(input)
    submarine.move()
    product = submarine.horizontal * submarine.depth
    print(f'Part 1: {product}')

    submarine.reset()
    submarine.moveWithAim()
    product = submarine.horizontal * submarine.depth
    print(f'Part 2: {product}')
