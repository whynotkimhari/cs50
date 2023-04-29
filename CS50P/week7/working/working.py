import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"^(\d\d?):?(\d?\d?)? (.)M to (\d\d?):?(\d?\d?)? (.)M$",s)
    if time:
        t1,m1,p1, t2,m2, p2 = time.groups()

        if m1 == "":
            m1 = 0
        if m2 == "":
            m2 = 0

        m1 = int(m1)
        m2 = int(m2)
        t1 = int(t1)
        t2 = int(t2)

        if m1 >= 60 or m2>= 60 or t1 > 12 or t2> 12:
            raise ValueError

        if t1 == 12:
            t1 = 0
        if t2 == 12:
            t2 = 0

        if p1 == "A" and p2 == "P":
            return f"{t1:02}:{m1:02} to {(t2+12):02}:{m2:02}"

        elif p1 =="A" and p2 == "A":
            return f"{t1:02}:{m1:02} to {t2:02}:{m2:02}"

        elif p1 == "P" and p2 == "A":
            return f"{(t1+12):02}:{m1:02} to {t2:02}:{m2:02}"

        elif p1 == "P" and p2 == "P":
            return f"{(t1+12):02}:{m1:02} to {(t2+12):02}:{m2:02}"

    raise ValueError

if __name__ == "__main__":
    main()