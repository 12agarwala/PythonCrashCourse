def make_album(Artist_name, Album_title):
    Dict = {'name': Artist_name, 'album': Album_title}
    return Dict
for i in range(3):
    Artist_name = input("Please enter the name of an artist: ")
    Album_title = input("Please enter the name of one of the artist's albums: ")
    x = make_album(Artist_name, Album_title)
    print(x)


