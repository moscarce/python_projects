number = 0
count = 1
product = 1
num1 = 0
num2 = 0
num3 = 0
num4 = 0
while(count < 5):
    num = int(input('Enter number: '))
    number += num
    count += 1
    product *= num
    if count == 2:
        num1 = num
    if count == 3:
        num2 = num
    if count == 4:
        num3 = num
    if count == 5:
        num4 = num

print('Sum = ',number)
print('Average = ',number/4)
print('Product = ', product)
if num1 <= num2 and num1 <= num3 and num1 <= num4:
    print(f'First number entered ({num1}) is the lowest number')
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    print(f'Second number entered ({num2}) is the lowest number')
elif num3 <= num2 and num3 <= num1 and num3 <= num4:
    print(f'Third number entered ({num3}) is the lowest number')
elif num4 <= num2 and num4 <= num3 and num4 <= num1:
    print(f'Fourth number entered ({num4}) is the lowest number')
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(f'First number entered ({num1}) is the largest number')
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print(f'Second number entered ({num2}) is the largest number')
elif num3 >= num2 and num3 >= num1 and num3 >= num4:
    print(f'Third number entered ({num3}) is the largest number')
elif num4 >= num2 and num4 >= num3 and num4 >= num1:
    print(f'Fourth number entered ({num4}) is the largest number')
