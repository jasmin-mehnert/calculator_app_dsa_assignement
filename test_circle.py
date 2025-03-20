import pytest
from math import pi
from circle import Circle 

def test_perimeter() -> None:
    # Tests the perimeter calculation for a Circle with radius 5
    circle = Circle(5)
    expected_perimeter = 2 * pi * 5
    assert circle.perimeter() == pytest.approx(expected_perimeter, rel=1e-5)

def test_area() -> None:
    # Tests the area calculation for a Circle with radius 5
    circle = Circle(5)
    expected_area = pi * 5 ** 2
    assert circle.area() == pytest.approx(expected_area, rel=1e-5)