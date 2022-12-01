import bisect

def solve(file):
    current_calories = 0
    top_three_calories = [0, 0, 0]
    with open(file) as input_file:
        for line in input_file:
            if line.strip():
                print(line.rstrip())
                current_calories = current_calories + int(line)
            else:
                bisect.insort(top_three_calories, current_calories)
                top_three_calories = top_three_calories[-3:]
                current_calories = 0
        bisect.insort(top_three_calories, current_calories)
        top_three_calories = top_three_calories[-3:]

    print(top_three_calories)
    return sum(top_three_calories)


if __name__ == '__main__':
    print(solve('input.txt'))
