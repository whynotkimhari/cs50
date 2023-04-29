x = input("File name: ").lower().strip()
if x[-3] =="g" and x[-2] == "i" and x[-1] =="f":
    print("image/gif")
elif (x[-3] =="j" and x[-2] == "p" and x[-1] =="g") or (x[-4] =="j" and x[-3] == "p" and x[-2] =="e" and x[-1] == "g"):
    print("image/jpeg")
elif x[-3] =="p" and x[-2] == "n" and x[-1] =="g":
    print("image/png")
elif x[-3] =="p" and x[-2] == "d" and x[-1] =="f":
    print("application/pdf")
elif x[-3] =="t" and x[-2] == "x" and x[-1] =="t":
    print("text/plain")
elif x[-3] =="z" and x[-2] == "i" and x[-1] =="p":
    print("application/zip")
else:
    print("application/octet-stream")

