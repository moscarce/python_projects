import random


def guess_number():
    right_number = random.randint(1, 10)
    number = int(input('Guess a number between 1 to 10: '))
    while number != right_number:
        if number < right_number:
            print('Too low, Try again')
        if number > right_number:
            print('Too high, Try again')
        if number == right_number:
            print('CONGRATULATION  You have guessed right')
            exit()
        number = int(input('Guess a number between 1 to 10: '))



guess_number()
# def fizz_buzz():
#     for number in range(1,101):
#         if (number % 3 == 0) and (number % 5 == 0):
#             print('FIZZ BUZZ')
#         elif number % 3 == 0:
#             print('FIZZ')
#         elif number % 5 == 0:
#             print('BUZZ')
#         else:
#             print(number)
#
#
# fizz_buzz()
def roller_coaster():
    height = float(input('What is your height: '))
    if height >= 6:
        age = int(input('What is your age: '))
        if age < 12:
            print(f'You are {age} years old and the price is 100')
        elif age < 61:
            print(f'You are {age} years old and the price is 200')
        else:
            print("It's a free ride")
            print('We are doing charity for old people')

    else:
        print('DISQUALIFIED')
        print('Anybody below 6 feet is not allowed to ride')


roller_coaster()

