print('exercise 1\t')
person_1 = {'name': 'Alex', 'city': 'krasnodar', 'age': 26}
person_2 = {'name': 'katty', 'city': 'krasnoyarsk', 'age': 30}
person_3 = {'name': 'daron', 'city': 'los angeles', 'age': 45}

people = [person_1, person_2, person_3]

for person in people:
    print('This is ' + person['name'].title() +
          '! He/she from '
          + person['city'].title() + ' and age is '
          + str(person['age'])
          + '. \n\t')

print('exercise 2\t')
pet_1 = {'name': 'Phobos', 'species': 'cat', 'age': 2, 'location': 'krasnodar', 'owner': 'dasha'}
pet_2 = {'name': 'loona', 'species': 'cat', 'age': 4, 'location': 'krasnodar', 'owner': 'sasha'}
pet_3 = {'name': 'joker', 'species': 'dog', 'age': 1, 'location': 'marianskaya', 'owner': 'olga'}
pet_4 = {'name': 'kokosamba', 'species': 'cat', 'age': 4, 'location': 'adler', 'owner': 'dasha'}
pets =[pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print('This is ' + pet['name'].title()
          + ". It's a "
          + pet['species']
          + '. It is '
          + str(pet['age'])
          + ' years old. '
          + "Now it's in "
          + pet['location'].title()
          + ". It's owned to "
          + pet['owner'].title() + '.\n\t')

print('exercise 3\t')
favorite_places = {'Berlin': person_1['name'], 'Adler': person_2['name'], 'los angeles': person_3['name']}

for key in favorite_places.keys():
    print(key.title() + ' is favorite place of ' + favorite_places[key].title())
print('\t')

print('exercise 4\t')
favorite_numbers = {person_1['name']: [42, 13], person_2['name']: [12, 13], person_3['name']: [666, 13]}
for key in favorite_numbers.keys():
    print('Favorite numbers of ' + key.title() + ' is:')
    for number in favorite_numbers[key]:
        print(number)
    print('\t')

print('exercise 4\t')
cities = {'berlin': {'country': 'germany', 'population': '10 millions', 'fact': 'best city in the world'},
          'los angeles': {'country': 'usa', 'population': '25 millions', 'fact': 'hometown of SOAD'},
          'adler': {'country': 'russia', 'population': '300 thousands', 'fact': 'should i live in this city?'}}
for key in cities.keys():
    up_key = key.title()
    print('Some information about ' + up_key + ':')
    print(up_key + ' is placed in ' + (cities[key])['country'].title())
    print('There are ' + (cities[key])['population'] + ' of people in ' + up_key)
    print('Fun fact: ' + (cities[key])['fact'])
    print('\t')