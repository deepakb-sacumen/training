import pytest
from calculator import add, subtract, multiply, divide, calculate

def test_add():
    """
    Test case for the add method
    """
    answer = add(5, 7)
    assert answer == 12

def test_subtract():
    """
    Test case for the subtract method
    """
    answer = subtract(10, 5)
    assert answer == 5

def test_multiply():
    """
    Test case for the multiply method
    """
    answer = multiply(5, 7)
    assert answer == 35

def test_divide():
    """
    Test case for the divide method
    """
    answer = divide(10, 2)
    assert answer == 5

def test_calculate():
    """
    Test case for the calculate method
    """
    answer = calculate(str(1), 2, 5)
    assert answer == 7
    