from typing import List
from Line import Line


class Graph:
    def __init__(self, m: int, n: int) -> None:
        self.verticalSize = m
        self.horizontalSize = n
        self.data = [[0 for i in range(self.horizontalSize)] for j in range(self.verticalSize)]

    def __repr__(self) -> None:
        strData = ''
        for row in self.data:
            for value in row:
                if not value:
                    strData += '.'
                else:
                    strData += str(value)
            strData += '\n'
        return strData
    
    def populate(self, lines: List[Line]) -> None:
        for line in lines:
            for point in line.points:
                self.data[point.y][point.x] += 1
    
    def countOverlaps(self) -> int:
        overlaps = 0
        for row in self.data:
            for value in row:
                if value > 1:
                    overlaps += 1
        return overlaps
