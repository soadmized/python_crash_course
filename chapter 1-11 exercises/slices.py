slices = list(range(1, 30, 2))
#print(third)

print("first three elements of list:")
for i in slices[-3:]:
    print(i)

#-------------------------------

my_pizza = ['pepperoni', '4 cheese', 'bacon']
#other_pizza = ['margarita', 'salami', 'seefood']
other_pizza = my_pizza[:]
my_pizza.append('mushrooms')
other_pizza.append('smth')
print('My favorite pizza is:')
for i in my_pizza:
    print(i)

print('Friend pizza is:')
for i in other_pizza:
    print(i)