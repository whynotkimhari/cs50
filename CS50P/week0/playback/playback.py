x = input()
for i in range(len(x)):
    if x[i] != " ":
        print(x[i], end ="")
    else:
        print("...", end = "")
print()