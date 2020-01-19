#  ----- even or odd
num = ''

while type(num) != int:
    try:
        num = int(input('Input your number: '))
    except ValueError:
        print("Your's input isn't number! Try again.")
div = num % 10
if div != 0:
    print(str(num) + ' не кратно 10 :(')
else:
    print(str(num) + ' кратно 10!')


# ------ pizza toppings

flag = True
print("\nHi! Which topping would you like to add to your pizza?")
topping = ''
while flag:
    topping = input("\n (Type 'quit' to exit): ")
    if topping == 'quit':
        break
    else:
        print('Ok, we will add ' + topping + ' to your pizza!')

# ------ cinema tickets

ratio = {0: range(0,3), 10: range(3,12), 15: range(12,100)}
flag = True
while flag:
    age = int(input('Input your age: '))
    if age in range(0,3):
        print('You get a free ticket! ')
    elif age in range(3,13):
        print('Your price is 10$!')
    elif age in range(13,120):
        print('Your price is 15$!')
    flag = False

# ------- mountain poll

responses = {}
poll_active = True

while poll_active:
    name = input('Input your name please: ')
    response = input('Input your vote ples: ')
    responses[name] = response
    repeat = input('Would you like to let another person to respond? yes/no: ')
    if repeat == 'no':
        poll_active = False
print(responses)

# ------- sandwiches + no pastrami

sandwiches = ['chicken', 'bacon', 'tuna', 'veggie', 'pastrami', 'pastrami', 'pastrami',]
finished_sandwiches = []
print('Unfortunately, we ran out of pastrami :((')

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

while sandwiches:
    current_sandwich = sandwiches.pop()
    finished_sandwiches.append(current_sandwich)
    print('Hey, I made you a {} sandwich!'.format(current_sandwich))

for sandwich in finished_sandwiches:
    print(sandwich)

