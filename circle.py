# create circle class with perimeter and area methods

from math import pi

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * pi * self.radius
    
    def area(self) -> float:
        return pi * self.radius ** 2