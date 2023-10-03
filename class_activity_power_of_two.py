def rearrange(question):
    answer = ''
    for element in question:
        for index, value in enumerate('kissdry'):
            if element == index:
                answer += value
                break
    return answer


print(rearrange([6, 2, 3, 4, 1, 0, 5]))
print(rearrange([0, 1, 2, 3, 4, 5, 6]))
