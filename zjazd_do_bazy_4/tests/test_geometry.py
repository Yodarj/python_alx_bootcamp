from zjazd_do_bazy_4.mathematica.geometry.figures import square_area
from zjazd_do_bazy_4.mathematica.geometry.figures import triangle_area as triangle

def test_square():
    assert square_area(5) == 25
    assert square_area(9) == 81

def test_triangle():
    assert triangle(2, 4) == 4
    assert triangle(5, 3) == 7.5