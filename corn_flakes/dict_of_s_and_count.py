import re


def dict_of_s(lst: list) -> dict:
    return {
        f'{elements}': lst.count(f'{elements}')
        for elements in lst
        if elements[0] in ['s', 'S']
    }


names = ['Joe','Daniel','Seyi','Sikiru','Muhammed','Hakimi','Segun','Ashley','Seyi']
print(dict_of_s(names))
