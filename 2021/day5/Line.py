from typing import List
from Point import Point

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        self.points = self._calculatePoints()

    def __repr__(self) -> None:
        return f'{self.start} -> {self.end}'

    def _calculatePoints(self) -> List[Point]:
        points = list()
        current = self.start
        while current != self.end:
            points.append(current)
            if self.start.x == self.end.x and self.start.y > self.end.y:
                # x1 == x2 and y1 > y2: decrement y
                current = Point(current.x, current.y - 1)
            elif self.start.x == self.end.x and self.start.y < self.end.y:
                # x1 == x2 and y1 < y2: increment y
                current = Point(current.x, current.y + 1)
            elif self.start.x > self.end.x and self.start.y == self.end.y:
                # x1 > x2 and y1 == y2: decrement x
                current = Point(current.x - 1, current.y)
            elif self.start.x < self.end.x and self.start.y == self.end.y:
                # x1 < x2 and y1 == y2: increment x
                current = Point(current.x + 1, current.y)
            elif self.start.x > self.end.x and self.start.y > self.end.y:
                # x1 > x2 and y1 > y2: decrement x and y
                current = Point(current.x - 1, current.y - 1)
            elif self.start.x > self.end.x and self.start.y < self.end.y:
                # x1 > x2 and y1 < y2: decrement x and increment y
                current = Point(current.x - 1, current.y + 1)
            elif self.start.x < self.end.x and self.start.y > self.end.y:
                # x1 < x2 and y1 > y2: increment x and decrement y
                current = Point(current.x + 1, current.y - 1)
            elif self.start.x < self.end.x and self.start.y < self.end.y:
                # x1 < x2 and y1 < y2: increment x and y
                current = Point(current.x + 1, current.y + 1)
            else:
                print(f'Error: invalid slope')
                exit()
        points.append(current)
        return points