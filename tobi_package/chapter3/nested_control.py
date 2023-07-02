largest = 0
second_largest = 0

for x in range(10):
    num = int(input('Enter number: '))
    if num > largest:
        second_largest = largest
        largest = num
print(f'Largest number: {largest}')
print(f'Second largest number: {second_largest}')
