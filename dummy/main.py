import pytest

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 3 * 4 == 12

def test_division():
    assert 8 / 4 == 2

# You can add more test functions here

if __name__ == "__main__":
    pytest.main(['-v', '--html=report.html'])
