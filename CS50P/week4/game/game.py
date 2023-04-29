from random import randint

list = []
level = "a"
guess = "a"

while True:
    try:
        if str(level).isnumeric() == False:
            level = input("Level: ")
        while str(level).isnumeric() == False or int(level) <= 0:
            raise TypeError()

        level = int(level)
        list.append(randint(1,level))
        break
    except TypeError:
        pass

while True:
    try:
        if str(guess).isnumeric() == False or int(guess) != list[0]:
            guess = input("Guess: ")
        while str(guess).isnumeric() == False or int(guess) <= 0 or int(guess) != list[0]:
            if str(guess).isnumeric() == True and int(guess) < list[0]:
                print("Too small!")

            elif str(guess).isnumeric() == True and int(guess) > list[0]:
                print("Too large!")
            raise TypeError()

        if int(guess) == list[0]:
            print("Just right!")
            break
    except TypeError:
        pass