import sys
from Line import Line
from Point import Point
from Graph import Graph

if len(sys.argv) < 2:
    print('Usage: python3 day4.py input-file')
    exit()


with open(sys.argv[1], 'r') as f:
    # Store the graph size
    m, n, = 0, 0

    # Store the lines
    noDiagonals = list()
    diagonals = list()
    for line in f:
        points = line.split(' ', 3)
        x1 = int(points[0].split(',', 2)[0])
        y1 = int(points[0].split(',', 2)[1])
        x2 = int(points[2].split(',', 2)[0])
        y2 = int(points[2].split(',', 2)[1])
        
        if x1 == x2 or y1 == y2:
            # only include horizontal and vertical lines for part 1
            noDiagonals.append(Line(Point(x1, y1), Point(x2, y2)))

        diagonals.append(Line(Point(x1, y1), Point(x2, y2)))

        # x is horizontal size
        if x1 > n:
            n = x1
        if x2 > n:
            n = x2
        
        # y is vertical size
        if y1 > m:
            m = y1
        if y2 > m:
            m = y2

    # Add 1 to graph sizes because size needs to be 1 greater than largest index
    m += 1
    n += 1
    
    part1 = Graph(m, n)
    part1.populate(noDiagonals)
    print(f'Part 1: {part1.countOverlaps()}')

    part2 = Graph(m, n)
    part2.populate(diagonals)
    print(f'Part 2: {part2.countOverlaps()}')
        
