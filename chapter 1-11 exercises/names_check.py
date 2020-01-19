current_users = ['Alex', 'Michael', 'Max', 'Denis', 'John']
new_users = ['diego', 'alex', 'MAX']

for name in new_users:
    name = name.lower()
    name = name.capitalize()
    if name in current_users:
        print('Sorry, this name is already in use :(')
    else:
        print('You use this name!')
        current_users.append(name)
print(current_users)
