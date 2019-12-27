def statment(user: int) -> int:
    string = user
    return  string


def make_shirt(size='M', text='I love Python'):
    print("You chose {0} size. There will be text '{1}' on your shirt!".format(size,text))


def album_info(artist, name, tracks=0):
    album = {'artist': artist, 'name': name}
    if tracks:
        album = {'artist': artist.title(), 'name': name.capitalize(), 'tracks': tracks}
    return album


def show_magicians(mag_list):
    for name in mag_list:
        print(name)


def make_great(mag_list):
    edited_list = []
    for name in mag_list:
        name = 'Great ' + name
        edited_list.append(name)
    print(edited_list)


def get_sandwich(*parts):
    print('\nYour sandwich consists of: \n')
    for part in parts:
        print(part)


def build_profile(first, last, **kwargs):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in kwargs.items():
        profile[key] = value
    return profile


def car_info(brand, model, **kwargs):
    info = {}
    info['brand'] = brand
    info['model'] = model
    for key, value in kwargs.items():
        info[key] = value
    return info