from typing import List


class Submarine:
    """We all live in a yellow submarine"""

    def __init__(self, course: List[str]):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.course = course

    def move(self):
        """Moves the submarine according to the provided course."""
        for instruction in self.course:
            direction, value = instruction.split()
            if direction == 'forward':
                self.horizontal += int(value)
            elif direction == 'up':
                self.depth -= int(value)
            elif direction == 'down':
                self.depth += int(value)

    def moveWithAim(self):
        """Moves the submarine using 'aim' to determine direction."""
        for instruction in self.course:
            direction, value = instruction.split()
            value = int(value)
            if direction == 'forward':
                self.horizontal += value
                self.depth += (self.aim * value)
            elif direction == 'up':
                self.aim -= value
            elif direction == 'down':
                self.aim += value

    def reset(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
