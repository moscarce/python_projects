first_name = input('Enter first name: ')
if first_name:
    name1 = first_name
else:
    print('your first name cannot be empty')
    exit()
if first_name:
    last_name = input('Enter last name: ')
if last_name:
    name2 = last_name
else:
    print('your last name cannot be empty')
    exit()
if name1 and name2:
    age = int(input('Enter your age: '))


if age < 0:
    print('Your name is ', name1, name2, 'and')
    print('your age is ',age, 'and your age cannot be a negative number')
elif age < 18:
    print('Your name is ', name1, name2, 'and')
    print('your age is ',age, 'and you are underage')
if age >= 65:
    print('Your name is ', name1, name2, 'and')
    print('your age is ',age, 'and you are old citizen')
if age >= 18 and age <= 64:
    print('Your name is ', name1, name2, 'and')
    print('your age is ',age, 'and you are a youth')