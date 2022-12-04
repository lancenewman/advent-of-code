def convert_ascii_to_priority(character):
    # a-z are ascii values 97-122, so transform them to 1-26 by subtracting 97.
    # A-Z are ascii values 65-90, so transform them to 27-52 by subtracting 38.
    return ord(character) - 96 if character.islower() else ord(character) - 38


def get_common_item_priority(rucksack):
    compartment1 = rucksack[:len(rucksack) // 2]
    compartment2 = rucksack[len(rucksack) // 2:]
    common_item = ''.join(set(compartment1).intersection(compartment2))
    return convert_ascii_to_priority(common_item)
    

def get_group_badge_priority(group):
    common_badge = ''.join(set(group[0]).intersection(group[1], group[2]))
    return convert_ascii_to_priority(common_badge)


def solve(file):
    with open(file, 'r') as input:
        total_rucksack_priority = 0
        total_badge_priority = 0
        group = []
        for line in input:
            rucksack = line.strip()
            total_rucksack_priority = total_rucksack_priority + get_common_item_priority(rucksack)
            group.append(rucksack)

            if len(group) == 3:
                total_badge_priority = total_badge_priority + get_group_badge_priority(group)
                group = []

    return (total_rucksack_priority, total_badge_priority)

if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')