from src.operation_math import add, sub


def test_add():
    assert add(3,4)==7
    assert add(-2,1)==-1

def test_sub():
    assert sub(5,1)==4
    assert sub(-3,3)==-0
