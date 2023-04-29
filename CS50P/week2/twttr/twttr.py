x = input("Input: ")
l = []

for i in range(len(x)):
    if x[i] != "a" and x[i] != "A" and x[i] != "e" and x[i] != "E" and x[i] != "o" and x[i] != "O" and x[i] != "i" and x[i] != "I" and x[i] != "u" and x[i] != "U":
        l.append(x[i])

print("Output: " + "".join(l))