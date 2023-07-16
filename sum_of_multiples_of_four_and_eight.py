sum_of_four = 0
for number in range(1, 5):
    if number % 4 == 0:
        for echo in range(1,6) :
            sum_of_four += (number ** echo)
print(sum_of_four,end=" ")
sum_of_eight = 0
for number in range(6, 9):
    if number % 8 == 0:
        for echo in range(1,6) :
            sum_of_eight += (number ** echo)
print(sum_of_eight)