dict = {}
while True:
    try:
        x = input()
    except EOFError:
        break
    if x.upper() not in dict:
        dict[x.upper()] = 1
    else:
        dict[x.upper()] += 1

sorted_dict = sorted(dict.items())

for key,values in sorted_dict:
    print(values, key)