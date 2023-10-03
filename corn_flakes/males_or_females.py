def gender_count(lst: list)->list:
    return [('Male',lst.count('Male')+lst.count('male')),('Female',lst.count('Female')+lst.count('female'))]

students = ['male','female','Female','Male','Male','male','female','male','female','male','female','male','female']

print(gender_count(students))
