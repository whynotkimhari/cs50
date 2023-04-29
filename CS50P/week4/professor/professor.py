import random

def main():
    le_vel = get_level()
    point = 0
    for i in range(10):
        X = generate_integer(le_vel)
        Y = generate_integer(le_vel)
        ANS = X + Y
        count_fail = 0
        while True:
            if count_fail == 3:
                count_fail = 0
                print(f"{X} + {Y} = {ANS}")
                break
            print(f"{X} + {Y} = ", end = "")
            ans = input()
            if count_fail != 3:
                if str(ans).isnumeric() == False:
                    print("EEE")
                    count_fail += 1
                elif str(ans).isnumeric() == True and int(ans) != ANS:
                    print("EEE")
                    count_fail += 1
                elif str(ans).isnumeric() == True and int(ans) == ANS:
                    point += 1
                    break
    print(f"Score: {point}")

def get_level():
    levels = ["1", "2", "3"]
    while True:
        level = input("Level: ")
        if level not in levels:
            continue
        return int(level)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()