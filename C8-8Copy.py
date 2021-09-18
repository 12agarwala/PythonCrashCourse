def make_album(Artist_name, Album_title):
    Dict = {'name': Artist_name, 'album': Album_title}
    return Dict
while True:
    Artist_name = input("Please enter the name of an artist: ")
    if Artist_name.upper() == 'Q':
        break
    else:
        Album_title = input("Please enter the name of one of the artist's albums: ")
        x = make_album(Artist_name, Album_title)
        print(x)

