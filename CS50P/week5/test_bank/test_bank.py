from bank import value

def main():
    test_bank_h_not_hello()
    test_bank_not_h()
    test_bank_hello()

def test_bank_h_not_hello():
    assert value("hi!") == 20
    assert value("Hi!") == 20

def test_bank_not_h():
    assert value("What's up?") == 100
    assert value("what's up?") == 100

def test_bank_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

if __name__ == "__main__":
    main()