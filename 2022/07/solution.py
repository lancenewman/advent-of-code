from anytree import Node, PreOrderIter
from typing import List, Tuple


def update_parent_sizes(file: Node, size: int) -> None:
    parent = file.parent
    if parent:
        parent.size = parent.size + size
        update_parent_sizes(parent, size)
    else:
        # At the root, everything is updated
        return


def execute_cd(target_dir: str, current_dir: Node) -> Node:
    if target_dir == '/':
        return current_dir

    if target_dir == '..':
        # Special case, change to parent
        return current_dir.parent

    # Try to find target in children
    for dir in current_dir.children:
        if dir.name == target_dir:
            return dir
    
    # Target dir is unreachable
    raise ValueError(f'Invalid target directory: {target_dir}')


def create_file_tree_from_input(input_lines: List[str]) -> Node:
    dir_tree = Node('/', size=0)
    current_dir = dir_tree
    for line in input_lines:
        contents = line.strip().split()
        if contents[0] == '$':
            # This is either a 'cd' or 'ls' command
            if contents[1] == 'cd':
                current_dir = execute_cd(contents[2], current_dir)
            else:
                # ls, just move to next line
                continue
        elif contents[0] == 'dir':
            # New directory, add it as a child node
            Node(contents[1], parent=current_dir, size=0)
        else:
            # File, add a leaf node & update parent sizes
            size = int(contents[0])
            file_node = Node(contents[1], parent=current_dir, size=size)
            update_parent_sizes(file_node, size)

    return dir_tree


def pick_dir_to_delete(root_dir: Node) -> int:
    total_space = 70000000
    required_free_space = 30000000
    total_used_space = root_dir.size
    total_free_space = total_space - total_used_space
    space_to_delete = required_free_space - total_free_space

    candidates = [d for d in PreOrderIter(root_dir) if not d.is_leaf and d.size >= space_to_delete]
    return min([d.size for d in candidates])


def get_dirs_under_size(dir_tree: Node, target_size: int) -> List[Node]:
    return [d for d in PreOrderIter(dir_tree) if d.children and target_size >= d.size]


def solve(file: str) -> Tuple[int, None]:
    with open(file, 'r') as input:
        dir_tree = create_file_tree_from_input(input.readlines())
        dirs_under_100k = get_dirs_under_size(dir_tree, 100000)
        dir_to_delete_size = pick_dir_to_delete(dir_tree)

    return(sum([d.size for d in dirs_under_100k]), dir_to_delete_size)


if __name__ == '__main__':
    part1, part2 = solve('input.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')