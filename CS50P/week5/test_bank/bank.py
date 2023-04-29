def main():
    x = input("Greeting: ")
    print(f"${value(x)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting[0] != "h":
        return 100
    elif "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20


if __name__ == "__main__":
    main()