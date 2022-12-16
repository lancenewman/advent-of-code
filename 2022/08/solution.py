from typing import List, Tuple


def calculate_scenic_score(target: int, subset: List[int]) -> int:
    score = 0
    for elem in subset:
        score = score + 1
        if elem >= target:
            break
    return score


def calculate_scenic_scores(grid: List[List[int]]) -> int:
    # init empty score array of same size as grid
    scores = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            look_left = calculate_scenic_score(tree, reversed(row[:j]))
            look_right = calculate_scenic_score(tree, row[j+1:])
            look_up = calculate_scenic_score(tree, reversed([r[j] for r in grid[:i]]))
            look_down = calculate_scenic_score(tree, [r[j] for r in grid[i+1:]])
            scores[i][j] = look_left * look_right * look_up * look_down
    return scores


def is_visible_in_subset(target: int, subset: List[int]) -> bool:
    for val in subset:
        if target <= val:
            return False
    return True


def is_visible(coords: Tuple[int,int], grid: List[List[int]]) -> bool:
    i, j = coords
    target = grid[i][j]
    row = grid[i]
    col = [row[j] for row in grid]

    visible_in_row = is_visible_in_subset(target, row[:j]) or is_visible_in_subset(target, row[j + 1:])
    visible_in_col = is_visible_in_subset(target, col[:i]) or is_visible_in_subset(target, col[i + 1:])
    return visible_in_row or visible_in_col


def count_visible_trees(grid: List[List[int]]) -> int:
    total_visible = 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if is_visible((i, j), grid):
                total_visible = total_visible + 1
    return total_visible


def construct_grid(input_lines: List[str]) -> List[List[int]]:
    return [[int(elem) for elem in line.strip()] for line in input_lines]


def solve(file):
    with open(file, 'r') as input_file:
        grid = construct_grid(input_file.readlines())

    total_visible_trees = count_visible_trees(grid)    
    max_scenic_score = max(map(max, calculate_scenic_scores(grid)))
    return (total_visible_trees, max_scenic_score)


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')