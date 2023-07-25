# password = input("Enter a password: ")
# while len(password) < 8:
#     password = input("Enter a password: ")
# print("Your password is secure, The length is", len(password))

name = 'tobi'
print(id(name))
name1 = ''
print(id(name1))
print(name1)
for i in name:
    name1 += i
    print(name1)
    print(id(name1))

print(name1)
print(id(name1))
