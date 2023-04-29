import sys
import inflect
from datetime import date


def main():
        user_input = check(input("Date of birth: "))
        to_day = date.today()
        print(find_minutes(to_day, user_input))


def find_minutes(to_day, user_input):
    mins = (to_day - user_input).days*24*60
    word = inflect.engine().number_to_words(mins).capitalize()
    return word.replace("and ", "") + " minutes"


def check(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()