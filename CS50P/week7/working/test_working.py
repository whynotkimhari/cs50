from working import convert
import pytest

def main():
    test_convert_one()
    test_convert_two()
    test_convert_three()

def test_convert_one():
    with pytest.raises(ValueError):
        convert(r"9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert(r"9 AM - 5 PM")
def test_convert_two():
    with pytest.raises(ValueError):
        convert(r"09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert(r"9?59 AM to 5?59 PM")
def test_convert_three():
    assert convert(r"9:59 AM to 5:59 PM") == "09:59 to 17:59"
if __name__ == "__main__":
    main()