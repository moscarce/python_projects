def factorial(number):
    numbers = number
    for x in range(1, number+1):
        if x < number:
            numbers *= (number-x)
    print(f'{number}! = {numbers}')


factorial(5)
factorial(10)
factorial(20)
factorial(30)
