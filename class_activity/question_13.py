def check_specified_value(value,lst:list)->bool:
    for elements in lst:
        if value == elements:
            return True
    return False

print(check_specified_value(3,[1,5,8,3]))
print(check_specified_value(-1,[1,5,8,3]))
