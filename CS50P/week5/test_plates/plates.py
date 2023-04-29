def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    count = 0
    count_c = 0
    char = ["a", "b", "c", "d"," e", "f"," g"," h" ,"i" ,"k" ," l", "m", "n", "o", "p", "q","r", "s"," t", "u", "v", "w"," x", "y", "z"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special = [" ", ".", ",", "!", "?"]

    if len(s) < 2 or len(s) > 6 or ((s[0].lower() and s[1].lower()) not in char):
        return False
    elif len(s) >= 2 and len(s) <= 6 and ((s[0].lower() and s[1].lower()) in char):
        for i in range(len(s)):
            if s[i] in special:
                return False
            elif s[i] in num:
                if s[i-1].lower() in char and s[i] =="0" or s[i+1] in special:
                    return False
                elif s[i-1].lower() in char and s[i] != "0":
                    cnt = 0
                    for j in range(i+1, len(s)):
                        if s[j].lower() in char:
                            cnt += 1
                    if cnt == 0:
                        return True
                    else:
                        return False
            elif s[i].lower() in char:
                count_c += 1
        if count_c == len(s):
            return True
if __name__ == "__main__":
    main()