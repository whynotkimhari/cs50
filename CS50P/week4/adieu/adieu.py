greet = "Adieu, adieu, to "
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        print()
        break

if len(names) == 1:
    print(greet + names[0])

elif len(names) == 2:
    print(greet + names[0] + " and " + names[1])

else:
    print(greet, end="")
    for i in range(len(names)):
        if i != len(names) -2 and i != len(names) - 1:
            print(names[i], end=", ")
        elif i == len(names) -2:
            print(names[i], end=", and ")
        elif i == len(names) - 1:
            print(names[i])