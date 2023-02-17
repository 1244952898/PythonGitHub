import os.path


def get_words():
    path=os.path.join('../','files/file.txt')
    with open(path,'r') as o:
       return o.readlines()

for s in get_words():
    print(s)