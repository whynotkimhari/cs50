from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar._capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar._size == 2


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(6)
    assert jar._size == 4

    jar = Jar()
    jar.deposit(8)
    with pytest.raises(ValueError):
        assert jar.withdraw(10)