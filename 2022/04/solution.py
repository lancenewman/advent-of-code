def extract_integer_bounds(assignment, delimiter='-'):
    return [int(bound) for bound in assignment.split(delimiter)]


def assignment_fully_covered(a1, a2, delimiter='-'):
    a1_lower_bound, a1_upper_bound = extract_integer_bounds(a1, delimiter)
    a2_lower_bound, a2_upper_bound = extract_integer_bounds(a2, delimiter)
    return a1_lower_bound <= a2_lower_bound and a1_upper_bound >= a2_upper_bound


def assignment_partially_covered(a1, a2, delimiter='-'):
    a1_lower_bound, a1_upper_bound = extract_integer_bounds(a1, delimiter)
    a2_lower_bound, a2_upper_bound = extract_integer_bounds(a2, delimiter)
    return a1_lower_bound <= a2_lower_bound <= a1_upper_bound or a2_lower_bound >= a1_upper_bound >= a2_upper_bound


def contains_partially_covered_section(assignments, delimiter=','):
    a1, a2 = assignments.split(delimiter)
    return assignment_partially_covered(a1, a2) or assignment_partially_covered(a2, a1)


def contains_fully_covered_section(assignments, delimiter=','):
    a1, a2 = assignments.split(delimiter)
    return assignment_fully_covered(a1, a2) or assignment_fully_covered(a2, a1)


def solve(file):
    with open(file, 'r') as input:
        fully_covered_sections = 0
        partially_covered_sections = 0
        for line in input:
            assignments = line.strip()
            if contains_fully_covered_section(assignments):
                fully_covered_sections = fully_covered_sections + 1
            
            if contains_partially_covered_section(assignments):
                partially_covered_sections = partially_covered_sections + 1
        return (fully_covered_sections, partially_covered_sections)


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')