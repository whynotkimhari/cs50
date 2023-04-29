# DAILY AMENITIES
#### Video Demo:  <URL https://www.youtube.com/watch?v=Y5MyPYDRaJE&t=3s>
#### Description:
About me: I am Kim Hải, Hari instead will be more easier to spell. I'm from Vietnam - wonderful country - must go destination.

How to use this project:

- First of all, requirements:
    """
    pip install pytube
    pip install pyqrcode
    python -m pip install git+https://gitlab.com/drj11/pypng@pypng-0.20220715.0
    pip install re
    pip install Pillow
    pip install pytest
    """

- Next, run it with 'python project.py' or 'python3 project.py' :
    +Then, there are four amenities here in my project. They are:
                                                                +) creating random password
                                                                +) getting the audio in the video from Youtube
                                                                +) creating the qr code for a link
                                                                +) making a pdf file by using png files

- Let's dive to each of them:
    <+> Checking to stop program <+>
    """
    while True:
        try:
            method = input("Please input method: ")
            methods = ["getpass", "getmp4", "getqr", "getpdf"]
            ...
            ...
        except EOFError:
            print()
            print("Thanks for using! ")
            break
    """

    These line of codes will catching when you want to stop the program using ctrl D (raising EOFError)

    <+> Checking valid input <+>

    """
    while True:
        try:
            method = input("Please input method: ")
            methods = ["getpass", "getmp4", "getqr", "getpdf"]
            try:
                if method not in methods:
                    raise NameError
            ...
            ...
            except NameError:
                print("Method does not exist!")
    """

    These line of codes will catching when you use the non-existed method (key). But it will not stop the program. It will let you re-input.

    <+> Creating random password <+>
        I will 'import string' and 'import random' to use this function, the codes are
            """
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
            """

            and

            """
            if method == "getpass":
                try:
                    your_pass = input("Password: ")
                    new_pass = Create_Random_Password(your_pass)
                    print(f"Your new pass is: {new_pass}")
                except ValueError:
                    print("You did not type any password!")
            """

            to catch exception.

    <+> Getting the audio in the video from Youtube <+>
        I will 'import pytube' and 'from pytube.exceptions import RegexMatchError' to use this function, the codes are

            """
            def MP3_from_MP4_Youtube(video_url):
            data = pytube.YouTube(video_url)
            audio = data.streams.get_audio_only()
            audio.download()
            return "Finished. Please check the folder to find .mp4 file"\
            """

            and

            """
            if method == "getmp4":
                try:
                    video_url = input("Please type the url: ")
                    print(MP3_from_MP4_Youtube(video_url))
                except RegexMatchError:
                    print("You typed a wrong url!")
            """

            to catch exception.

    <+> Creating the qr code for a link <+>
        I will 'import re', 'import pyqrcode', 'import png', and 'from pyqrcode import QRCode' to use this function, the codes are
            """
            def Create_QRCode_for_link(link, name_of_qr):
            if len(name_of_qr) == 0:
                raise ValueError
            url = pyqrcode.create(link)
            url.png(f"{name_of_qr}.png", scale=6)
            return "Finished. Please check the folder to find your QR code"
            """

            and

            """
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
            """

            to catch exception.

    <+> Making a pdf file by using png files <+>
        I will 'from PIL import Image' to use this function, the codes are
            """
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
            """

            and

            """
            if method == "getpdf":
                try:
                    amount = int(input("PNGs: "))
                    print(PNG_to_PDF(amount))
                except IOError:
                    print("Something went wrong. Please double-check!")
            """

            to catch exceptions.


- The next one is test_project.py:
    I will 'import pytest'
    and 'from project import Create_Random_Password, MP3_from_MP4_Youtube, Create_QRCode_for_link, PNG_to_PDF'
    and 'from pytube.exceptions import RegexMatchError'
    to use this file, the codes are:

        In main function:
            """
            def main():
                test_Create_Random_Password()
                test_MP3_from_MP4_Youtube()
                test_Create_QRCode_for_link()
                test_PNG_to_PDF()
            """

            and to run main:

            """
            if __name__ == "__main__":
                main()
            """

        In test_Create_Random_Password():
            """
            def test_Create_Random_Password():
                assert len(Create_Random_Password('HAI')) == 3
                with pytest.raises(ValueError):
                    Create_Random_Password("")
            """

            one to check if true, one to check if raise an error.

        In test_MP3_from_MP4_Youtube():
            """
            def test_MP3_from_MP4_Youtube():
                with pytest.raises(RegexMatchError):
                    MP3_from_MP4_Youtube('s')
                assert MP3_from_MP4_Youtube('https://www.youtube.com/watch?v=2f3YZJbOf2c&list=RD2f3YZJbOf2c&start_radio=1') == "Finished. Please check the folder to find .mp4 file"
            """

            one to check if true, one to check if raise an error.

        In test_Create_QRCode_for_link():
            """
            def test_Create_QRCode_for_link():
                with pytest.raises(ValueError):
                    Create_QRCode_for_link('', '')
                assert Create_QRCode_for_link('https://www.youtube.com/watch?v=2f3YZJbOf2c&list=RD2f3YZJbOf2c&start_radio=1', 'music') == "Finished. Please check the folder to find your QR code"
            """

            one to check if true, one to check if raise an error.

        In test_PNG_to_PDF():
            """
            def test_PNG_to_PDF():
                with pytest.raises(IOError):
                    PNG_to_PDF(0)
            """

            to check if raise an error.