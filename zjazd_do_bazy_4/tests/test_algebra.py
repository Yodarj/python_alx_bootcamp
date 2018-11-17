import pytest

from zjazd_do_bazy_4.mathematica.algebra.matrices import add_matrices
from zjazd_do_bazy_4.mathematica.algebra.matrices import sub_matrices


def test_add_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6], ]

    b = [
        [7, 8, 9],
        [10, 11, 12], ]

    result = add_matrices(a, b)

    assert result == [
        [8, 10, 12],
        [14, 16, 18], ]


def test_add_matrices_with_different_count_of_rows():
    a = [
        [1,2,3],
        [4,5,6],
        [6,5,3]
    ]

    b = [
        [7,8,9],
        [10,11,12],
    ]

    with pytest.raises(ValueError) as e:
        add_matrices(a,b)

def test_add_matrices_with_different_count_of_columns():
    a = [
        [1,2,3],
        [4,5,6]
    ]

    b = [
        [7,8,9,12],
        [10,11,12,10],
    ]

    with pytest.raises(ValueError) as e:
        add_matrices(a,b)


def test_sub_matrices():
    a = [
    [1, 2, 3],
    [4, 5, 6], ]

    b = [
    [7, 8, 9],
    [10, 11, 12], ]

    result = sub_matrices(a, b)

    assert result == [
    [-6, -6, -6],
    [-6, -6, -6], ]
