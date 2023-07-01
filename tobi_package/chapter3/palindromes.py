while True:
    numbers = input('Enter five digit number: ')
    if len(numbers) == 5:
        number = int(numbers)
        for x in range(5):
            digit = number % 10
            number = number // 10
            if x == 0:
                fifth_digit = digit
            elif x == 1:
                fourth_digit = digit
            elif x == 2:
                third_digit = digit
            elif x == 3:
                second_digit = digit
            elif x == 4:
                first_digit = digit
        if first_digit == fifth_digit and second_digit == fourth_digit:
            print(f'{numbers} is a palindrome')
        else:
            print(f'{numbers} is not a palindrome')
        exit()
    print('Please kindly enter exactly five digit number')
