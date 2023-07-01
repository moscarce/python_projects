number = -1
while(True):
    valid_input = int(input("Enter a number between 1 or 2: "))
    number += 1
    if (valid_input==1 or valid_input==2):
        print(f'''
        CONGRATULATIONS YOU WON AFTER FAILING {number} TIME(S)''')
        exit()