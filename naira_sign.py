def triangle(num):
    for a in range(num):
        for b in range(a + 1):
            print("#", end=" ")
        for b in range(num - a):
            print(" ", end=" ")
        for b in range(num - a):
            print("#", end=" ")
        for b in range(a+1):
            print(" ", end=" ")
        for b in range(a + 1):
            print(" ", end=" ")
        for b in range(num-a):
            print("#", end=" ")
        for b in range(num - a):
            print(" ", end=" ")
        for b in range(a+1):
            print("#", end=" ")
        print()


triangle(10)
picture = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
for x in picture:
    for y in x:
        print('# ',end='') if y == 1 else print('  ',end='')
    for y in x:
        print('# ',end='') if y == 0 else print('  ',end='')
    print()



