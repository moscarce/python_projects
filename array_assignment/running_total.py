numbers = [1, 2, 3, 4, 5]
random_numbers = [5, 2, 9, 5, 7, 9, 10, 1, 20]


def compute_running_total(list: list):
    running_total = []
    total = 0
    for num in list:
        total += num
        running_total.append(total)
    print(f'The running total of {list} is {running_total}')


compute_running_total(numbers)
compute_running_total(random_numbers)
