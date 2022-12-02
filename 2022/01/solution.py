import bisect

def solve(file):
    current_calories = 0
    top_three_calories = [0, 0, 0]
    with open(file) as input_file:
        for line in input_file:
            if line.strip():
                current_calories = current_calories + int(line)
            else:
                bisect.insort(top_three_calories, current_calories)
                top_three_calories = top_three_calories[-3:]
                current_calories = 0
        bisect.insort(top_three_calories, current_calories)
        top_three_calories = top_three_calories[-3:]

    return top_three_calories


if __name__ == '__main__':
    top_three = solve('input.txt')
    print(f'Part 1: {max(top_three)}')
    print(f'Part 2: {sum(top_three)}')
