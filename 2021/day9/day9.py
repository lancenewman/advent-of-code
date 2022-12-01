from operator import itemgetter


def main():
    graph = [[int(x) for x in line.strip()]
             for line in open('day9/input.txt').readlines()]

    h = len(graph)
    w = len(graph[0])

    # Part 1
    riskLevel = 0
    for y in range(h):
        for x in range(w):
            num = graph[y][x]
            if x > 0 and graph[y][x-1] <= num:
                continue
            if x < w-1 and graph[y][x+1] <= num:
                continue
            if y > 0 and graph[y-1][x] <= num:
                continue
            if y < h-1 and graph[y+1][x] <= num:
                continue
            riskLevel += 1 + num
    print(f'Part 1: {riskLevel}')

    # Part 2
    basins = {}
    basinSizes = {}

    def visit(x, y, basin):
        if graph[y][x] == 9:
            return
        if (x, y) in basins:
            return
        basins[(x, y)] = basin
        basinSizes[basin] += 1
        if x > 0 and graph[y][x-1] != 9:
            visit(x-1, y, basin)
        if x < w-1 and graph[y][x+1] != 9:
            visit(x+1, y, basin)
        if y > 0 and graph[y-1][x] != 9:
            visit(x, y-1, basin)
        if y < h-1 and graph[y+1][x] != 9:
            visit(x, y+1, basin)

    basin = 0
    for y in range(h):
        for x in range(w):
            basinSizes[basin] = 0
            visit(x, y, basin)
            basin += 1

    largest = dict(
        sorted(basinSizes.items(), key=itemgetter(1), reverse=True)[:3])

    answer = 1
    for _, size in largest.items():
        answer *= size
    print(f'Part 2: {answer}')


if __name__ == '__main__':
    main()
