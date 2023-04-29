inp = input("Fraction: ")
x = "a"
y = "b"
check = True
for i in range(len(inp)):
    if inp[i] == "/":
        x, y = inp.split("/")
        break
    elif inp[i].isnumeric() == True:
        continue
    elif inp[i].isnumeric() == False and inp[i] != "/":
        check = False

while(x.isnumeric() == False or y.isnumeric() == False or y == "0" or int(x) > int(y) or check == False):
    inp = input("Fraction: ")

perc = round((int(x) / int(y) ) * 100)

if perc >= 99:
    print("F")
elif perc <= 1:
    print("E")
else:
    print(str(perc) + "%")