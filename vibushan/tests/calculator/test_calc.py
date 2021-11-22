"""This file contains the test codes for calc.py"""
import pytest
from calculator.calc import Calc, calculate

def test_calc_operations():
    res = Calc(3,4)
    assert res.add() == 7
    assert res.subtract() == -1
    assert res.multiply() == 12
    assert res.divide() == 0.75

def test_calculate():
    operation_key = 'add'
    num1 = int(3)
    num2 = int(4)
    assert calculate(operation_key, num1, num2) == 7

def test_calculate_negative():
    operation_key = 'Add'
    num1 = int(3)
    num2 = int(4)
    with pytest.raises(ValueError):
        assert calculate(operation_key, num1, num2) == 7
