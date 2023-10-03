def greatest_common_divisor(first_number:int,second_number:int):
    min = first_number
    if second_number < first_number:
        min = second_number
    for number in range(2,min):
        if first_number % number == 0 and second_number % number == 0:
            return number
    return 'No Greatest Common Divisor'

print(greatest_common_divisor(10,20))
print(greatest_common_divisor(4,16))
print(greatest_common_divisor(10,15))
print(greatest_common_divisor(10,13))
