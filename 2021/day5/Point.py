class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> None:
        return f'{self.x},{self.y}'
    
    def __eq__(self, point) -> bool:
        return self.x == point.x and self.y == point.y

    def __ne__(self, point) -> bool:
        return not self == point