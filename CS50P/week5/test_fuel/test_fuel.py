from fuel import convert, gauge
import pytest

def main():
    test_invalid_input()
    test_zero_input()
    test_valid()

def test_invalid_input():
    with pytest.raises(ValueError):
        convert("dog/cat")

def test_zero_input():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valid():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

if __name__ == "__main__":
    main()