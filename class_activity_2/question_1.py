color_list_1 = set(['white','black','red'])
color_list_2 = set(['red','green'])
print(set(elements for elements in color_list_1 if elements not in color_list_2))
print(color_list_1.difference(color_list_2))
