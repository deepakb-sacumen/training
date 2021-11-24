from src.calculator import add, subtract, multiple, devide
def test_add():
    a=10
    b=5
    result = add(a,b)
    assert result == 15

def test_subtract():
    a=10
    b=5
    result = subtract(a,b)
    assert result == 5

def test_multiple():
    a=10
    b=5
    result = multiple(a,b)
    assert result == 50

def test_devide():
    a=10
    b=5
    result = devide(a,b)
    assert result == 2