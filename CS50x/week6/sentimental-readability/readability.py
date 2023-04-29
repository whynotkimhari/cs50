# TODO
from cs50 import get_string

letter = 0
word = 1
sentence = 0

text = get_string("Please insert the text: ")


for i in range(len(text)):
    if text[i].isalpha() == True:
        letter += 1

for i in range(len(text)):
    if text[i] == " ":
        word += 1

for i in range(len(text)):
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        sentence += 1

L = (float(letter) / float(word)) * 100
S = (float(sentence) / float(word)) * 100
index = (0.0588 * L - 0.296 * S - 15.8)
q = int(round(index))

if q >= 16:
    print("Grade 16+")

elif q < 1:
    print("Before Grade 1")

else:
    print(f"Grade {q}")