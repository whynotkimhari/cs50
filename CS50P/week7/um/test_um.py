from um import count

def main():
    test_um_one()
    test_um_two()
    test_um_three()

def test_um_one():
    assert count(r"Um, thanks for the album.") == 1
    assert count(r"um?") == 1

def test_um_two():
    assert count(r"Um, thanks, um...") == 2

def test_um_three():
    assert count("yummy") == 0
    assert count("   um   ,um,") == 2

if __name__ == "__main__":
    main()