Amount_due = 50

while Amount_due > 0:
    print("Amount due: ", Amount_due)
    insert_coin = int(input("Insert coin: "))
    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        Amount_due -= insert_coin

if Amount_due <= 0:
    print("Change owed:", -Amount_due)