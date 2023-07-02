number = 0
count = 1
product = 1
num1 = 0
num2 = 0

while count < 4:
    num = int(input('Enter number: '))
    number += num
    if count == 1:
        num2 += num
    count += 1
    product *= num
    if num > num1:
        num1 = num
    if num < num2:
        num2 = num

print(f'({num2}) is the lowest number')
print(f'({num1}) is the largest number')
print('Sum = ', number)
print('Average = ', number/3)
print('Product = ', product)
