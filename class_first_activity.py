numbers = [10, 20, 30, 40, 50]
sum = 0
for x in numbers:
    sum += x
print(sum)

sum = 0
for y in numbers[::2]:
    sum += y
print(sum)

sum = 0
for y in numbers[1::2]:
    sum += y
print(sum)

squares = []
for i in numbers:
    i = i ** 2
    squares.append(i)
print(squares)

max = squares[4]
min = squares[4]
for z in squares:
    if z > max:
        max = z
    if z < min:
        min = z
difference = max - min
print(squares)
print(squares)
print(difference)

difference = squares[len(squares)-1] - squares[0]
print(difference)

sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)


def my_sort(number):
    sort = []
    for x in range(len(number)):
        min = number[0]
        for y in number:
            if y < min:
                min = y
        number.remove(min)
        sort.append(min)
    return sort


number = [8, 2, 5, 6, 1, 3, 9, 4, 7, 10, 20, 10]
print(my_sort(number))
result = [i for i in number if i % 2 == 0]
print(result)
for i in range(len(number)):
    for j in range(len(number)):
        if number[j] > number[i]:
            number[j],number[i] = number[i],number[j]
    print(number)
numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
print(numbers[::-1])

result = []
for x in range(len(numbers)-1,-1,-1):
    result.append(numbers[x])
print(result)
