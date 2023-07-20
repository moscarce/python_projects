# def divide_or_square(number: int):
#     return round(number**0.5, 2) if number % 5 == 0 else number % 5
#     # if number % 5 == 0:
#     #     return round(number**0.5, 2)
#     # else:
#     #     return number % 5
#
#
# print(divide_or_square(10))
# print(divide_or_square(25))
# print(divide_or_square(16))
# print(divide_or_square(30))
# print(divide_or_square(121))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [i for i in numbers if i % 2 == 0]
print(result)
result = [i**2 for i in numbers]
print(result)