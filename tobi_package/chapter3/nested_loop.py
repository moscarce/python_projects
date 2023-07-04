for x in range(1, 5):
    for y in range(1, 11):
        print('*' * y) if x % 2 == 1 else print('*' * (11-y))
    print()