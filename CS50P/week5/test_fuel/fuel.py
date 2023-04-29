def main():
    inp = input("Fraction: ")
    perc = convert(inp)
    ans = gauge(perc)
    print(ans)

def convert(fraction):
    while True:
        try:
            x ,y = fraction.split("/")
            nx = int(x)
            ny = int(y)
            f = nx /ny
            if f <= 1:
                return int(f*100)
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()