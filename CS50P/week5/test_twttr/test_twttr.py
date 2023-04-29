from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("facebook") == "fcbk"
    assert shorten("FACEBOOK") == "FCBK"
    assert shorten("520") == "520"
    assert shorten("???") == "???"

if __name__ == "__main__":
    main()