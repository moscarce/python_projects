while True:
    numbers = input('Enter five digit number: ')
    if len(numbers) == 5:
        number = int(numbers)
        for x in range(5):
            digit = number % 10
            number = number // 10
            print(digit,end='\t')
        exit()
    print('Please kindly enter exactly five digit number')