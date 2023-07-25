# create a function that takes a parameter which take a list of integers as argument and return the highest odd number in the list
def highest_odd(lst: list) -> int:
    # use list comprehension to grab the odd numbers in the list
    odd_numbers = [number for number in lst if number % 2 == 1]
    # I have to iterate through the comprehended list and get the highest odd number
    # step1 = create a variable that takes the first element in the comprehended list
    max = odd_numbers[0]
    # step2 = iterate through the comprehended list and assign the highest number to max
    for number in odd_numbers:
        if number > max:
            max = number
    # return max as it is now the highest number in the list
    return max


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101]
print(highest_odd(numbers))
print()
def highest_odd_one_line(lst: list)-> int:
    num = max([i for i in lst if i % 2 == 1])
    return num
print(highest_odd_one_line(numbers))