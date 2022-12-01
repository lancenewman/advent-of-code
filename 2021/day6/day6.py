import sys

from School import School

if len(sys.argv) < 2:
    print('Usage: python3 day6.py input-file')

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = list(map(int, data[0].strip().split(',')))
    print(
        f'Part 1: {School([data.count(i) for i in range(9)]).modelGrowth(80)}')
    print(
        f'Part 2: {School([data.count(i) for i in range(9)]).modelGrowth(256)}')
