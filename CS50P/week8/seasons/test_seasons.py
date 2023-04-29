import seasons
import pytest
from datetime import date

def main():
    test_mins()

def test_mins():
    with pytest.raises(SystemExit):
        assert seasons.check("2020/11/17")
    with pytest.raises(SystemExit):
        assert seasons.check("999999999-9999999999-999999999999")

    assert seasons.find_minutes(date.fromisoformat("2022-11-17"),date.fromisoformat("2020-11-17")) == "One million, fifty-one thousand, two hundred minutes"
if __name__ == "__main__":
    main()