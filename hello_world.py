msg = "Hello world!"
print(msg)

#-----------------

name = "Alex"
msg1 = "Hello, "
msg2 = "! Would you like to learn some Python today?"
print(msg1 + name + msg2)

#-----------------

name = 'alex'
print(name, name.title(), name.upper())

#----------------------------

friends = ['oleg', 'john', 'vitya', 'timur']
for i in friends:
	print(i.title())

#-----------------------------

print('\n____________ \nLIST EXSERCIZES \n__________________________')
guest_list = ['Daron', 'Shavo', 'Adam']
msg = '! You are invited for my dinner!'
for i in range(len(guest_list)):
	text = 'Dear ' + guest_list[i] + msg
	print(text)

print('\nCrap! Daron is busy. New guest is timur\n')
guest_list[0] = friends[3].title()
for i in range(len(guest_list)):
	text = 'Dear ' + guest_list[i] + msg
	print(text)

print('\nNew dinner table! I can invite more friends!\n')

#guest_list = guest_list + friends.remove('timur')
print(guest_list)