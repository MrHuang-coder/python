def make_album(name, album_name, song_num=''):
    """"返回一个字典, 其中包含有关一个人的信息"""
    song = {'editor': name, 'album': album_name}
    if song_num:
        song['song_num'] = song_num
    return song
album_one = make_album('huanghaitao', 'dengjia', 5)
album_two = make_album('dengjia', 'huanghaitao')
album_three = make_album('xuezhiqian', 'cheng', '5')
print(album_one)
print(album_two)
print(album_three)
