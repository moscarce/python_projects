##create a function that takes a collection as argument
##create a variable call count and initialize it as 0
##iterate through list and let the variable increase its count by 1 at each iteration, return the variable

def length(collection)->int:
    count = 0
    for i in collection:
        count += 1
    return count


try_list = [1,2,3,4,5,6]
try_string = 'Tobiloba'
try_set = {1,2,3,4}
try_tuple = (1,2,3,'test')
print(length(try_list))
print(length(try_string))
print(length(try_set))
print(length(try_tuple))

