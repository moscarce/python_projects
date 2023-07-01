input('What is your problem? ')
answer = input('Have you had this problem before (yes or no)? ')
if answer.capitalize() == 'Yes':
    print('Well, you have it again.')
elif answer.capitalize() == 'No':
    print('Well, you have it now.')
else:
    print('invalid answer')