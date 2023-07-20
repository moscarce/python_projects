numbers = [1, 2, 3, 4, 5]
random_numbers = ['A', 'B', 'C', 'D', 'E']


def alternatively_take_list(list_1: list, list_2:list):
    result = []
    list_1_count = 0
    list_2_count = 0
    size = len(list_1) + len(list_2)
    for index in range(size):
        if index % 2 == 0:
            result.append(list_1[list_1_count])
            list_1_count += 1
        else:
            result.append(list_2[list_2_count])
            list_2_count += 1
    print(result)


alternatively_take_list(numbers, random_numbers)
