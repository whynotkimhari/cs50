import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    x = input("Input: ")
    figlet.setFont(font = choice(fonts))
    print("Output: " + figlet.renderText(x))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        else:
            x = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print("Output:")
            print(figlet.renderText(x))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")