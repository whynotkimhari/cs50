# TODO
from cs50 import get_int

h = get_int("Height: ")

while h < 1 or h > 8:
    h = get_int("Height: ")

w = h * 2 + 2

for i in range(h):
    for j in range(w):
        if j == h:
            print(" ", end="")
        elif j == h + 1:
            print(" ", end="")

        elif j < h:
            if i + j >= h - 1:
                print("#", end="")
            if i + j < h - 1:
                print(" ", end="")
        elif j > h + 1:
            if i >= j - (h + 2):
                print("#", end="")
    print()