import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    output = []
    try:
        list = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append(row)

        for mini_dict in list:
            last, first = mini_dict["name"].split(",")
            first = first.strip()
            last = last.strip()
            output.append({"first": first, "last": last, "house": mini_dict["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file2:
        writer = csv.DictWriter(file2, fieldnames = ["first","last","house"])
        writer.writeheader()
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})