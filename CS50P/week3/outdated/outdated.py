months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    check_type = 0
    try:
        date = input("Date: ").strip()

        for i in range(len(date)):
            if date[i] == "/":
                check_type += 1

        if check_type == 2:
            MM, DD, YYYY = date.split("/")
            if MM.isnumeric() == True and DD.isnumeric() == True and YYYY.isnumeric() == True and int(DD) <= 31 and int(MM) <= 12:
                MM = int(MM)
                DD = int(DD)
                pass
            else:
                raise TypeError()

        elif check_type == 0:
            DD_check = []
            count = 0
            MM, DD, YYYY = date.split(" ")

            for i in range(len(DD)):
                if DD[i] != ",":
                    DD_check.append(DD[i])
                else:
                    count += 1

            if count == 0:
                raise TypeError()

            preDD = "".join(DD_check)
            if preDD.isnumeric() == True:
                DD = int(preDD)

            if preDD.isnumeric() == False:
                raise TypeError()
            if DD > 31:
                raise TypeError()

            if MM not in months:
                raise TypeError()

            for i in range(len(months)):
                if MM == months[i]:
                    MM = i + 1

        else:
            raise TypeError()

        print(f"{YYYY}" + "-", end="")
        print(f"{MM:02}" + "-", end="")
        print(f"{DD:02}")
        break

    except TypeError:
        pass
