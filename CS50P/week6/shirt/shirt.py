import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    list = [".png" , ".jpg", ".jpeg"]
    if os.path.splitext(sys.argv[1].lower())[1] not in list or os.path.splitext(sys.argv[2].lower())[1] not in list:
        sys.exit("Invalid input")

    elif os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
        sys.exit("Input and output have different extensions")

    else:
        try:
            image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    ans = ImageOps.fit(image, size)
    ans.paste(shirt,shirt)
    ans.save(sys.argv[2])