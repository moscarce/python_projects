# Create a function that takes list as an argument
# iterate through the list then and remove an element from the list then iterate through the list after removing the element to check if there is another one of
# there
# if there is another one there, you return the element else return no duplicate

fruits = ['apple', 'orange', 'banana', 'apple']
name = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicate(lst: list):
    for x in lst:
        lst.remove(x)
        for y in lst:
            if x == y:
                return x
        lst.append(x)
    return 'No duplicate'


print(check_duplicate(fruits))
print(check_duplicate(name))
print(fruits)