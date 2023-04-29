# TODO
from cs50 import get_int
h = get_int("Height: ")
while h < 1 or h > 8:
    h = get_int("Height: ")

for i in range(h):
    for j in range(h):
        if i + j < h - 1:
            print(" ", end="")
        elif i + j >= h - 1:
            print("#", end="")
    print()