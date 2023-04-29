def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    list = []
    cnt = 0
    for i in range(1, len(d)):
        if d[i] != ".":
            list.append(float(d[i]))
            cnt += 1
        else:
            list.append(float(d[i+1])/10)
            list.append(float(d[i+2])/100)
            break
    for j in range(0, cnt):
        list[j] *= pow(10,cnt - 1 - j)
    return sum(list)

def percent_to_float(p):
    # TODO
    list = []
    for i in range(0, len(p) - 1):
        list.append(float(p[i])*pow(10, len(p) - 2 - i))
    return sum(list)/100

main()