import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    else:
        try:
            count = 0
            with open(sys.argv[1]) as file:
                for row in file:
                    row = row.strip()
                    if row != "" and row.startswith("#") == False:
                        count += 1
            print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")