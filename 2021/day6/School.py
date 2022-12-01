from typing import List


class School:
    """Represents a school of fish"""
    STARTING_GROWTH_RATE = 6

    def __init__(self, fish: List[int]) -> None:
        self.fish = fish

    def modelGrowth(self, days: int) -> int:
        for i in range(days):
            count = self.fish.pop(0)
            self.fish[6] += count
            self.fish.append(count)
        return sum(self.fish)
