import re


def collect_string():
    string = input('Enter a string\n')
    return string

def collect_number_of_times():
    number = input('Enter number of times\n')
    while not number.isnumeric():
        print('Please enter a positive integer')
        number = input('Enter number of times\n')
    return int(number)


def print_string():
    inputted_string = collect_string()
    number_of_times = collect_number_of_times()
    if len(inputted_string) < 2:
        for x in range(number_of_times):
            print(inputted_string)
    else:
        print(f'{inputted_string[0]}{inputted_string[1]}')

print_string()



