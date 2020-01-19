aliens = []
alien_0 = {'color': 'green', 'points': 5}
alien_0['points'] = 10
alien_0['x_position'] = 25
alien_0['y_position'] = 2000
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2, alien_1, alien_2]

for alien in range(30):
    aliens.append(alien_0)
for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
for alien in aliens:
    print(alien)


for i, j in alien_0.items():
    print(i, j)

# -------------------------
string = 'qwerty'
print(string.title())
print(string.capitalize())
# -------------------------
favourite_lang = {'sarah': 'python',
                  'john': 'c++',
                  'max': 'ruby',
                  'alex': 'python',
                  'serj': 'java'}
friends = ['kelly', 'max', 'alex']
anon = 'Billy'
for name in favourite_lang.keys():
    if name in friends:
        print('Hi ' + name.title() +
              "! I can see you favourite language is " +
              favourite_lang[name].title() + '!')
if anon not in favourite_lang:
    print(anon.title() + ', please put you fav lang')

print('---------------------------------')
for name in favourite_lang:
    print('Thank you ' + name.title() + ' for taking the poll!')
for name in friends:
    if name not in favourite_lang:
        print(name.title() + ', please take the poll')
