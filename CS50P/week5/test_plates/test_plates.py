from plates import is_valid

def main():
    test_too_short_long_plates()
    test_two_first_not_char()
    test_punctuation()
    test_not_zero_first()
    test_number_middle()
    test_legit()

def test_too_short_long_plates():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_two_first_not_char():
    assert is_valid("23") == False
    assert is_valid("A2") == False

def test_punctuation():
    assert is_valid("BAG,.?") == False

def test_not_zero_first():
    assert is_valid("BAG023") == False

def test_number_middle():
    assert is_valid("BAF8A") == False

def test_legit():
    assert is_valid("CS50") == True

if __name__ =="__main__":
    main()