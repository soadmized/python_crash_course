from module_8 import *


if __name__ == '__main__':
    make_shirt()
    make_shirt('S', 'IEAIAIO')
    album = album_info('System of a Down', 'NEW ALBUM')
    print(album)
    while True:
        artist = input('Input artist name (Press q anytime to quit): ')
        if artist == 'q':
            break
        album_name = input('Input album name: ')
        if album_name == 'q':
            break
        tracks = int(input('Input count of tracks: '))
        if tracks == 'q':
            break

        album = album_info(artist, album_name, tracks)
        print(album)
    mag_list = ['Dave', 'Ted', 'John', 'Alex']
    show_magicians(mag_list)
    make_great(mag_list)
    get_sandwich('bread', 'pepperoni', 'green peppers')
    get_sandwich('bun', 'bacon')
    print('\n')
    user_profile = build_profile('Sam', 'Sepiol', location='NY', field='hackerman')
    print(user_profile)
    car = car_info('Chevrolet', 'Camaro', price=35000, type='coupe')
    print(car)
