import validator_collection

def main():
    email = input("What's your email address? ")
    print(check(email))

def check(s):
    try:
        email_address = validator_collection.validators.email(s)
    except (validator_collection.errors.EmptyValueError, validator_collection.errors.InvalidEmailError):
        return "Invalid"
    return "Valid"

if __name__ == "__main__":
    main()