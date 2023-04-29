import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if 'title' in s:
        analys = re.search(r'^<iframe(?:.+)src="https?://(?:www\.)?(.+)/embed/(.+)"(?: title)(?:.+)?></iframe>$',s)
    else:
        analys = re.search(r'^<iframe(?:.+)src="https?://(?:www\.)?(.+)/embed/(.+)"></iframe>$',s)

    if analys:
        utub, code = analys.groups()
        if utub == "youtube.com":
            utub = "youtu.be/"
        else:
            return None
        return "https://" + utub + code
    return None

if __name__ == "__main__":
    main()