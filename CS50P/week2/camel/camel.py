x = input("camelCase: ")
l = []
for i in range(len(x)):
    if x[i].isupper() == True and i != 0:
        l.append("_" + x[i].lower())
    else:
        l.append(x[i])

print("".join(l))