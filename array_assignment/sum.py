numbers = [1, 2, 3, 4, 5]
random_numbers = [5, 2, 9, 5, 7, 9, 10, 1, 20]


def for_loop_total(list: list):
    total = 0
    for num in list:
        total += num
    print(f'The total sum of {list} is {total}')


for_loop_total(numbers)
for_loop_total(random_numbers)


def while_loop_total(list: list):
    index = 0
    total = 0
    while index < len(list):
        total += list[index]
        index+=1
    print(f'The total sum of {list} is {total}')


while_loop_total(numbers)
while_loop_total(random_numbers)
