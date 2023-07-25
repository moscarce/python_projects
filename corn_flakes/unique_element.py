##Write a function that takes a list as parameter removes the duplicates in the list and return the list with unique element
##iterate through the list and remove an element from the list
##iterate through the after removing and check if any other element is equal to the removed one
##if any other element is equal to the removed element,then you remove the element that is equal to it
##then append the removed element back

def unique_list(lst:list)->list:
    for element in lst:
        lst.remove(element)
        for equal_element in lst:
            if element == equal_element:
                lst.remove(equal_element)
        lst.append(element)
    return lst


numbers_list = [1,1,2,3,4,4,5]
string_list = ['hello','peter','hello','hi','tobi',]
unique_number_list = [4,8,9,2,7]
unique_string_list = ['4','8','9','2','7']
print(unique_list(numbers_list))
print(unique_list(string_list))
print(unique_list(unique_number_list))
print(unique_list(unique_string_list))