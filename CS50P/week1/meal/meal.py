def main():
    time = input("What time is it? ")
    time2 = convert(time)

    if time2 >= 7 and time2 <= 8:
        print("breakfast time")
    elif time2 >= 12 and time2 <= 13:
        print("lunch time")
    elif time2 >= 18 and time2 <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    ih = float(h)
    im = float(m)
    return ih + im/60


if __name__ == "__main__":
    main()