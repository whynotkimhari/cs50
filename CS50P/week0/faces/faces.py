def convert(x):
    list = []
    for i in range(len(x)):
        list.append(x[i])
    for i in range(len(list) - 1):
        if list[i] == ":":
                if list[i+1] == ")":
                    list[i] = "🙂"
                    list[i+1] = ""
                elif list[i+1] == "(":
                    list[i] = "🙁"
                    list[i+1] = ""
    y = "".join(list)
    return y

def main():
    x = input()
    y = convert(x)
    print(y)

if __name__ == "__main__":
    main()