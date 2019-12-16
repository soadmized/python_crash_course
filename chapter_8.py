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


if __name__ == '__main__':
    make_shirt()
    make_shirt('S', 'IEAIAIO')
    album = album_info('System of a Down', 'NEW ALBUM')
    print(album)
    while True:
        artist = input('Input artist name: ')
        album_name = input('Input album name: ')
        tracks = input('Input count of tracks \n(Press q anytime to quit):')
        if (artist == 'q') or (album_name == 'q') or (tracks == 'q'):
            break
        else:
            album = album_info(artist, album_name, tracks)
        print(album)
