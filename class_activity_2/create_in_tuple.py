def create_tuple(lst: list, lst2: list) -> list:
    output = []
    length = len(lst)
    if length > len(lst2):
        length = len(lst2)
    for index in range(length):
        output.append((lst[index], lst2[index]))
    for index in range(length,len(lst)):
        output.append((lst[index],))
    for index in range(length,len(lst2)):
        output.append((lst2[index],))
    return output


l1 = [1, 2, 3, 4, 5, 11,12 ]
l2 = [6, 7, 8, 9, 10]
print(create_tuple(l1, l2))
l3 = [1, 2, 3, 4, 5 ]
l4 = [6, 7, 8, 9, 10,11,12]
print(create_tuple(l3, l4))
