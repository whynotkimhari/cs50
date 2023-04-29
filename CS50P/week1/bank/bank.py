x = input("Greeting: ").lower().strip()

if x[0] != "h":
    print("$100")
else:
    if x[1] == "e" and x[2] == "l" and x[3] == "l" and x[4] == "o":
        print("$0")
    else:
        print("$20")