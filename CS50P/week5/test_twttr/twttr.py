def main():
    x = input("Input: ")
    print("Output: " + shorten(x))

def shorten(word):
    l = []
    vowels = ["a", "e", "u", "i" ,"o"]
    for i in range(len(word)):
        if word[i] not in vowels:
            l.append(word[i])
    return "".join(l)

if __name__ == "__main__":
    main()