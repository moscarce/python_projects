numbers = [1, 2, 3, 4, 5]
random_numbers = [5, 2, 9, 5, 7, 9, 10, 1]


def largest_number(number=[]):
    max_number = number[0]
    for num in number:
        if num > max_number:
            max_number = num
    print(f'Largest number is {max_number}')


largest_number(numbers)
largest_number(random_numbers)
