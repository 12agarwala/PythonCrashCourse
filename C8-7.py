def make_album(Artist_name, Album_title, Songs = ''):
    Dict = {'name': Artist_name, 'album': Album_title, '# of songs': Songs}
    return Dict
for i in range(3):
    Artist_name = input("Please enter the name of an artist: ")
    Album_title = input("Please enter the name of one of the artist's albums: ")
    Songs = input("Please enter the total number of song in the album: ")
    x = make_album(Artist_name, Album_title, Songs)
    print(x)


