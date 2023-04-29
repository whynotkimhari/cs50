import string
import random

import pytube
from pytube.exceptions import RegexMatchError

import re
import pyqrcode
import png
from pyqrcode import QRCode

from PIL import Image

def main():
    while True:
        try:
            method = input("Please input method: ")
            methods = ["getpass", "getmp4", "getqr", "getpdf"]
            try:
                if method not in methods:
                    raise NameError

                if method == "getpass":
                    try:
                        your_pass = input("Password: ")
                        new_pass = Create_Random_Password(your_pass)
                        print(f"Your new pass is: {new_pass}")
                    except ValueError:
                        print("You did not type any password!")

                if method == "getmp4":
                    try:
                        video_url = input("Please type the url: ")
                        print(MP3_from_MP4_Youtube(video_url))
                    except RegexMatchError:
                        print("You typed a wrong url!")

                if method == "getqr":
                    try:
                        link = input("Please type the link: ")
                        check = re.search(r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", link)
                        if check:
                            name_of_qr = input("Please type a name for QR: ")
                            print(Create_QRCode_for_link(link, name_of_qr))
                        else:
                            raise ValueError
                    except ValueError:
                        print("Something went wrong. Please double-check!")

                if method == "getpdf":
                    try:
                        amount = int(input("PNGs: "))
                        print(PNG_to_PDF(amount))
                    except IOError:
                        print("Something went wrong. Please double-check!")

            except NameError:
                print("Method does not exist!")

        except EOFError:
            print()
            print("Thanks for using! ")
            break

def Create_Random_Password(your_pass):
    size = len(your_pass)
    if size == 0:
        raise ValueError
    lower_case=string.ascii_lowercase
    upper_case=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    big_string = lower_case+upper_case+digits+symbols
    ran_pass= random.sample(big_string, size)
    return ''.join(ran_pass)


def MP3_from_MP4_Youtube(video_url):
    data = pytube.YouTube(video_url)
    audio = data.streams.get_audio_only()
    audio.download()
    return "Finished. Please check the folder to find .mp4 file"

def Create_QRCode_for_link(link, name_of_qr):
    if len(name_of_qr) == 0:
        raise ValueError
    url = pyqrcode.create(link)
    url.png(f"{name_of_qr}.png", scale=6)
    return "Finished. Please check the folder to find your QR code"

def PNG_to_PDF(amount):
    if amount == 0:
        raise IOError
    img1 = ""
    image_list = []
    for i in range(amount):
        name_of_png = input("Name of png file: ")
        image = Image.open(r'/workspaces/108981453/CS50P/project/' + name_of_png + '.png').convert('RGB')
        if i != 0 :
            image_list.append(image)
        else:
            img1 = image
    img1.save(r'/workspaces/108981453/CS50P/project/mypdf.pdf', save_all=True, append_images=image_list)
    return "Finished. Please check the folder to find your PDF"

if __name__ == "__main__":
    main()