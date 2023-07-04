number = 1101
decimal = 0
for x in range(4):
    digit = number % 10
    number = number // 10
    print(f'({digit} * {2**x}) +', end=' ') if x<3 else print(f'({digit} * {2**x})', end='')
    binary = digit * 2**x
    decimal += binary
print()
print(decimal)