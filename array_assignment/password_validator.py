import re


def validate_password():
    while True:
        password = input('Enter password:\n')
        if len(password) < 8:
            print('Invalid password')
            print('The password must be 8 characters long')
        elif not (re.search(r'[a-z]', password)):
            print('Invalid password')
            print('You need at least 1 lower case')
        elif not (re.search(r'[A-Z]', password)):
            print('Invalid password')
            print('You need at least 1 uppercase')
        elif not (re.search(r'[0-9]', password)):
            print('Invalid password')
            print('You need at least 1 digit')
        elif not (re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\|\\]', password)):
            print('Invalid password')
            print('You need at least 1 special character')
        else:
            return password


print(validate_password())
