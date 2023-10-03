def intersection(lst1 : list, lst2 : list)->tuple:
    return tuple(x for x in lst1 for y in lst2 if x == y)



print(intersection([1,2,3,7,8,9,0,6],[5,2,0,1,6]))
