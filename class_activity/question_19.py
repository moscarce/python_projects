def lowest_common_multiple(first_number:int,second_number:int):
    lcm = first_number * second_number
    for number in range(1,lcm):
        if number % first_number == 0 and number % second_number == 0:
            return number
    return lcm

print(lowest_common_multiple(10,20))
print(lowest_common_multiple(4,16))
print(lowest_common_multiple(10,15))
print(lowest_common_multiple(10,13))
print(lowest_common_multiple(2,2))
print(lowest_common_multiple(4,6))