import pytest
from Calculator.calculator import (Test_calculator)


calc = Test_calculator(6,3)

def test_add():
    res = calc.add()
    assert 9 == res

def test_sub():
    res = calc.sub()
    assert 3 == res

def test_mul():
    res = calc.mul()
    assert 18 == res

def test_div():
    res = calc.div()
    assert 2 == res

def test_switch_add():
    operation = '1'
    res = calc.switch(operation)
    assert 9 == res

def test_switch_sub():
    operation = '2'
    res = calc.switch(operation)
    assert 3 == res

def test_switch_mul():
    operation = '3'
    res = calc.switch(operation)
    assert 18 == res

def test_switch_div():
    operation = '4'
    res = calc.switch(operation)
    assert 2 == res


def test_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        calc = Test_calculator(4, 0)
        assert calc.div() == 2


def test_type_error():
    with pytest.raises(TypeError):
        calc = Test_calculator(6,3)
        assert calc.div(4, 0) == 2
        
