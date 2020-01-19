items = [1, 2, 3, 4, 5, 6]
for item in items:
	print(item)

#---------------------

my_list = list(range(1, 1000001))
'''for i in my_list:
	print(i)'''

print(sum(my_list))

#------------------

my_list = list(range(1, 20, 2))
print(my_list)

#------------------

my_list = list(range(3, 31, 3))
for digit in my_list:
	print(digit)


#------------------

my_list = list(range(1, 11))
third = []
for i in my_list:
	third.append(i**3)
print(third)

third = [value**3 for value in range(1, 11)]
print(third)
