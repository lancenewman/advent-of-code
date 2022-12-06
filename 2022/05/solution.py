from typing import Dict, List, Tuple


def parse_crate_stacks(crate_stacks_string: str) -> List[List[str]]:
    lines = crate_stacks_string.split('\n')
    rows = []
    for line in lines:
        # Chunk the string in 4-char increments
        row = [line[i:i+4].strip() for i in range(0, len(line), 4)]
        rows.append(row)
    
    num_stacks = len(rows[0])
    stacks = [[] for i in range(num_stacks)]

    # Go through the rows except the last one that contains stack numbers
    for row in rows[:-1]:
        for i in range(num_stacks):
            if row[i]:
                # Insert at bottom of stack to preserve order because we're
                # iterating from top to bottom
                stacks[i].insert(0, row[i][1])
    
    return stacks

        
def parse_moves(moves_string: str) -> List[Dict[str,int]]:
    moves = []
    for instruction in moves_string.split('\n'):
        instruction_words = instruction.split()
        move = {
            'amount': int(instruction_words[1]),
            'from': int(instruction_words[3]) - 1,  # subtract 1 for list indexing
            'to': int(instruction_words[5]) - 1
        }
        moves.append(move)
    return moves


def move_crates(starting_crate_stacks: List[List[str]], moves: List[Dict[str,int]], crane_version: str='9000') -> List[List[str]]:
    for move in moves:
        amount = move['amount']
        origin = move['from']
        destination = move['to']

        if crane_version == '9000':
            for _ in range(amount):
                crate = starting_crate_stacks[origin].pop()  # Removes from end of list
                starting_crate_stacks[destination].append(crate)  # Pushes to end of list
        else:
            stacks_to_move = starting_crate_stacks[origin][-amount:]
            starting_crate_stacks[destination] = starting_crate_stacks[destination] + stacks_to_move
            starting_crate_stacks[origin] = starting_crate_stacks[origin][:len(starting_crate_stacks[origin]) - amount]

    return starting_crate_stacks


def get_top_crates_string(crate_stacks: List[List[str]]) -> str:
    return ''.join([stack[-1] for stack in crate_stacks])
    

def solve(file: str) -> Tuple[str,str]:
    with open(file, 'r') as input:
        crate_string, move_string = input.read().split('\n\n')
        moves = parse_moves(move_string)
    
    moved_crate_stacks_v9000 = move_crates(parse_crate_stacks(crate_string), moves)
    moved_crate_stacks_v9001 = move_crates(parse_crate_stacks(crate_string), moves, crane_version='9001')
    return (get_top_crates_string(moved_crate_stacks_v9000), get_top_crates_string(moved_crate_stacks_v9001))


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')