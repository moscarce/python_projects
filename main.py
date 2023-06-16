import random

counter = 0
while counter < 10:
    number = int(input('You have 10 trials to guess a number between 1 to 10 : '))
    guessed_number = random.randint(1, 10)
    print('THE CORRECT NUMBER IS ', guessed_number ,'AND YOU GUSSED', number ,'SO')
    if number == guessed_number:
        print('YOU WON')
        exit()
    else:
        print('YOU LOSE, YOU HAVE', 9 - counter ,'TRIALS LEFT')

    counter += 1

