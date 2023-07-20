numbers = [1, 2, 3, 4, 5]
random_numbers = [5, 2, 9, 5, 7, 9, 10, 1, 20]


def find_element(list: list, element: str):
    for num in list:
        if num == element:
            print(f'{element} is in the list')
            return
    print(f'{element} is not in the list')


find_element(random_numbers, 10)
find_element(numbers, 10)
