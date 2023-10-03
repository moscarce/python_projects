def sum_list(lst: list, value: int) -> list:
    for x in range(len(lst)):
        for y in range(len(lst)):
            if x == y:
                continue
            if lst[x] + lst[y] == value:
                return [x, y]


l1 = [5, 4, 9, 7, 2, 0]
print(sum_list(l1, 16))
