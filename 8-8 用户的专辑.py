def make_album(singer, album_name):
    """"返回包含专辑和歌手名字的字典"""
    ablum = {'singer': singer, 'name': album_name}
    return ablum
while True:
    print("\nPlease tell me about your favorite album:")
    print("(enter 'q' at any time to quit)")

    singer = input("singer: ")
    if singer == 'q':
        break

    album_name = input("album_name: ")
    if singer == 'q':
        break

    album = make_album(singer, album_name)
    print("Your favorite album is %s that is %s sing" % (album['singer'], album['name']));
