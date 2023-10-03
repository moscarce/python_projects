def concatenate_list(lst:list)->str:
    output = ''
    for element in lst:
            output += str(element)
    return output


print(concatenate_list(['a','b',2,'c']))