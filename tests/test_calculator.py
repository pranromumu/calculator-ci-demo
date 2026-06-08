from calculator import add, subtract, multiply, divide, power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Error: Division by zero"

def test_large_numbers():
    assert multiply(1000000, 1000000) == 1000000000000

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 1) == 10