def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    for i in range(len(names)):
        names[i] += ' the Great'
names = ['hanhan', 'xiaozhu', 'hero']
show_magicians(names)
make_great(names)
show_magicians(names)