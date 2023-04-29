import requests
import sys
import json

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    if is_float(sys.argv[1]) == False:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    usd = float(o['bpi']['USD']['rate_float'])

    ans = usd * float(sys.argv[1])
    print(f"${ans:,.4f}")
def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
