def split_third(lst:list)->list:
    return [lst[::3],lst[1::3],lst[2::3]]


sample = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
print(split_third(sample))