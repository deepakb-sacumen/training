import pytest 
from calc.calculator import addition,subtraction,multiplication,division


def test_addition():
    assert addition(5,8) == 13
    assert addition(2,-2) == 0
    assert addition(0,0) == 0
    assert addition(-1,-1) == -2


def test_substraction():
    assert subtraction(5,8) == -3
    assert subtraction(2,-2) == 4
    assert subtraction(-2,-2) == 0
    assert subtraction(2,0) == 2
    assert subtraction(0,-2) == 2

def test_multiplication():
    assert multiplication(2,3) == 6
    assert multiplication(0,4) == 0
    assert multiplication(2,-3) == -6
    assert multiplication(-3,-3) == 9

def test_division():
    assert division(10,5) == 2
    assert division(1,2) == 0.5
    assert division(1,-2) == -0.5
    assert division(-10,-2) == 5
    with pytest.raises(ZeroDivisionError):
        assert division(10,0)
    with pytest.raises(TypeError):
        assert division('a',2)
    with pytest.raises(TypeError):
        assert division(3,'a')
    with pytest.raises(TypeError):
        assert division(1, 2, 3)
    with pytest.raises(TypeError):
        assert division('a','b')