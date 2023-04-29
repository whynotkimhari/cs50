# TODO
from cs50 import get_int


number = get_int("Number: ")
str_number = str(number)

numbers = []

for i in range(len(str_number)):
    k = number / (10 ** i)

    # check if the remain greater than .5
    if k - round(k) < 0:
        k = round(k) - 1
    else:
        k = round(k)

    # compute the digit
    digit = k % 10

    # add digit to list numbers
    numbers.append(digit)

# reverse the list
numbers.reverse()

# compute the sum
list_evens = []
list_odds = []
for j in range(len(numbers)):
    if j % 2 == 0:
        if numbers[j] * 2 >= 10:
            list_evens.append((numbers[j] * 2) // 10)
            list_evens.append((numbers[j] * 2) % 10)
        else:
            list_evens.append(numbers[j] * 2)
    else:
        list_odds.append(numbers[j])

sum = sum(list_evens) + sum(list_odds)

# check if valid
if sum % 2 == 0:
    if len(numbers) == 15:
        if numbers[0] == 3 and (numbers[1] == 4 or numbers[1] == 7):
            print("AMEX")
    elif len(numbers) == 16:
        if numbers[0] == 4:
            print("VISA")
        elif numbers[0] == 5 and (numbers[1] in [1, 2, 3, 4, 5]):
            print("MASTERCARD")
    elif len(numbers) == 13 and numbers[0] == 4:
        print("VISA")
else:
    print("INVALID")