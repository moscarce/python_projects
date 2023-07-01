for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
# At first it checks the state of row which is 0 at first then the inner loop check if 0%2==1 which is not, the inner for loop prints the else statement 10 times
# then it goes back to check value of row again which is now 1 and perform 1%2==1 which is true and performs the if statement
# then goes on and on till the outer loop gets to 9 and stop when the outer loop become false at 10