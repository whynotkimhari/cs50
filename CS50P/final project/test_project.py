import pytest
from project import Create_Random_Password, MP3_from_MP4_Youtube, Create_QRCode_for_link, PNG_to_PDF
from pytube.exceptions import RegexMatchError

def main():
    test_Create_Random_Password()
    test_MP3_from_MP4_Youtube()
    test_Create_QRCode_for_link()
    test_PNG_to_PDF()

def test_Create_Random_Password():
    assert len(Create_Random_Password('HAI')) == 3
    with pytest.raises(ValueError):
        Create_Random_Password("")

def test_MP3_from_MP4_Youtube():
    with pytest.raises(RegexMatchError):
        MP3_from_MP4_Youtube('s')
    assert MP3_from_MP4_Youtube('https://www.youtube.com/watch?v=2f3YZJbOf2c&list=RD2f3YZJbOf2c&start_radio=1') == "Finished. Please check the folder to find .mp4 file"

def test_Create_QRCode_for_link():
    with pytest.raises(ValueError):
        Create_QRCode_for_link('', '')
    assert Create_QRCode_for_link('https://www.youtube.com/watch?v=2f3YZJbOf2c&list=RD2f3YZJbOf2c&start_radio=1', 'music') == "Finished. Please check the folder to find your QR code"

def test_PNG_to_PDF():
    with pytest.raises(IOError):
        PNG_to_PDF(0)

if __name__ == "__main__":
    main()