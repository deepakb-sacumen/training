from calculator import addition, subtraction, mul, division


def test_add():
    assert addition(2, 3) == 5


def test_subtraction():
    assert subtraction(3, 2) == 1


def test_mul():
    assert mul(2, 2) == 4


def test_division():
    assert division(10, 5) == 2