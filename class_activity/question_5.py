def first_name():
    name = input('Enter firstname\n')
    while not name.isalpha():
        print('Invalid name')
        name = input('Enter firstname\n')
    return name

def last_name():
    name = input('Enter lastname\n')
    while not name.isalpha():
        print('Invalid name')
        name = input('Enter lastname\n')
    return name

def reverse(firstname,lastname):
    print(firstname[::-1],' ',lastname[::-1])


reverse(first_name(),last_name())