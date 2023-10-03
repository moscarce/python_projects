def single_number(lst):
    for x in lst:
        lst.remove(x)
        if x not in lst:
            return x
        lst.append(x)


first_input = [2,2,1]
second_input = [4,3,2,2,3,3]
third_input = [1]
print(single_number(first_input))
print(single_number(second_input))
print(single_number(third_input))

# for x in first_input:
#     if first_input.count(x) == 1:
#         return x

