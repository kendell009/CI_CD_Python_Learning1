from src.main import add, subtract

def test_add_function():
    assert add(2,3) == 5
    assert add(6,6) == 12
    assert add(4,4) == 8
    assert add(0,0) == 0


def test_subtract_function():
    assert subtract(6,3) == 3
    assert subtract(120, 60) == 60
    assert subtract(10,5) == 5


