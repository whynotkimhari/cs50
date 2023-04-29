from numb3rs import validate

def main():
    test_numb3rs_more_less()
    test_numb3rs_char()
    test_numb3rs_sastify()

def test_numb3rs_more_less():
   assert validate(r"0.1.2") == False
   assert validate(r"0.1") == False
   assert validate(r"0") == False
   assert validate(r"512.1.1.1") == False
   assert validate(r"1.512.1.1") == False
   assert validate(r"1.1.512.1") == False
   assert validate(r"1.1.1.512") == False

def test_numb3rs_char():
    assert validate(r"cat") == False
    assert validate(r"cat.dog.meo.meo") == False

def test_numb3rs_sastify():
    assert validate(r"255.255.255.255") == True
    assert validate(r"0.1.2.3") == True

if __name__ == "__main__":
    main()