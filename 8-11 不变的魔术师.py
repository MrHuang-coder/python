def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    for i in range(len(names)):
        names[i] += ' the Great'
    return names
names = ['hanhan', 'xiaozhu', 'hero']
show_magicians(names)
names_copy = make_great(names[:])
show_magicians(names)
show_magicians(names_ copy)