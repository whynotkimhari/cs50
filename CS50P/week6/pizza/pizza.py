import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    try:
        list = []
        #using csv.reader
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                list.append(row)
        print(tabulate(list, headers = "firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")