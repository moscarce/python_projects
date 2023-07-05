# for i in range(2):
#     value = int(input('Enter an integer (-1 to break): '))
#     print('You entered:', value)
#     if value == -1:
#         break
# else:
#     print('The loop terminated without executing the break')
def astericks(num):
    for x in range(1, num):
        for y in range(num-x):
            print(' ',end='')
        for y in range(x-1):
            print('*',end='')
        for y in range(x-1):
            print('*',end='')
        for y in range(num-x):
            print(' ',end='')
        print()
    for a in range(1, num):
        for b in range(a):
            print(' ', end='')
        for y in range(num - a):
            print('*', end='')
        for y in range((num - a)-1):
            print('*', end='')
        for y in range(a):
            print(' ', end='')
        print()

astericks(6)