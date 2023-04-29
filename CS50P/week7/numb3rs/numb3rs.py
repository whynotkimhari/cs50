import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    address = re.search(r"^(\d?\d?\d)\.(\d?\d?\d)\.(\d?\d?\d)\.(\d?\d?\d)$",ip)
    if address:
        d = address.groups()
        for d_i in d:
            if int(d_i) < 0 or int(d_i) > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()