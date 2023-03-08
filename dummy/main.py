import pytest

def test_addition():
    assert 2+2 == 4

def test_subtraction():
    assert 5-2 == 3

def test_multiplication():
    assert 3*4 == 12

def test_division():
    assert 8/2 == 4

if __name__ == '__main__':
    pytest.main(['-v', '-s', '--html=report.html'])
