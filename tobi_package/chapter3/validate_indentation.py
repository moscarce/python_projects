# grade = 93
# if grade >= 90:
#     print('A')
# print('Great Job!')
#    print('Take a break from studying')
#  No i won't expect tabnanny to flag it as error, but it should flag the next print as an error
import sys

# def collect():
#     num = int(input('number:'))
#     return num;
# def sum2():
#     total = 0
#     for i in range(1, collect()+1):
#         total += i
#     print(total)
# sum2()

# def highest_number(number1, number2, number3, number4):
#     if number1 >= number2 and number1 >= number3 and number1 >= number4:
#         maximum = number1
#         print(f'Largest number : {maximum}')
#     if number2 >= number1 and number2 >= number3 and number2 >= number4:
#         maximum = number2
#         print(f'Largest number : {maximum}')
#     if number3 >= number1 and number3 >= number2 and number3 >= number4:
#         maximum = number3
#         print(f'Largest number : {maximum}')
#     if number4 >= number1 and number4 >= number3 and number4 >= number2:
#         maximum = number4
#         print(f'Largest number : {maximum}')
#
#
# def lowest_number(number1, number2, number3, number4):
#     if number1 <= number2 and number1 <= number3 and number1 <= number4:
#         minimum = number1
#     elif number2 <= number1 and number2 <= number3 and number2 <= number4:
#         minimum = number2
#     elif number3 <= number1 and number3 <= number2 and number3 <= number4:
#         minimum = number3
#     elif number4 <= number1 and number4 <= number3 and number4 <= number2:
#         minimum = number4
#     print(f'Lowest number : {minimum}')
#
#
# highest_number(4, 2, 3, 4)

highest = -sys.maxsize - 1
second_highest = -sys.maxsize - 1

for i in range(5):
    num = int(input(':'))
    if num>highest:
        highest = num
        second_highest = highest
print(second_highest)
print(highest)


