names = ['admin', 'Alex', 'Eric', 'Max', 'Igor']
#names = []
if names:
    for name in names:
        if name == 'admin':
            print('Hello ' + name + '! Would ypu like to see status report?')
        else:
            print('Hello ' + name + '! Welcome back!')
else:
    print('We need some users!')