from src.main import add

def test_add_function():
    assert add(2,3) == 5
    assert add(6,6) == 12
    assert add(4,4) == 8
    assert add(0,0) == 2


