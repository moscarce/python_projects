def even_or_odd():
    number = input('Enter Number\n')
    while not number.isnumeric():
        print('Invalid input')
        number = input('Enter Number\n')
    number = int(number)
    return 'Even Number' if number%2 == 0 else 'Odd Number'


print(even_or_odd())
