# Write a function that takes a list as parameter removes the duplicates in the list and return the list with unique element
# Create an empty list in the function and iterate over the list that is passed in and add any one that is not in the empty list
# to the list and return the list


def unique_list(lst:list)-> list:
    result = []
    for element in lst:
        if element not in result:
            result += [element]
    return result

# def unique_list(lst:list) -> list:
#     return [element for element in lst if lst.count(element) < 2]




numbers_list = [1,1,2,3,4,4,5]
string_list = ['hello','peter','hello','hi','tobi',]
unique_number_list = [4,8,9,2,7]
unique_string_list = ['4','8','9','2','7']
print(unique_list(numbers_list))
print(unique_list(string_list))
print(unique_list(unique_number_list))
print(unique_list(unique_string_list))