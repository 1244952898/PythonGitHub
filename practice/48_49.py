import os
from glob import *
from pathlib import Path


# 48返回该文件夹中所有文件的路径
def get_all_folders(s_path: str, s='-'):
    for c_path in os.listdir(s_path):
        new_path = os.path.join(s_path, c_path)
        if os.path.isdir(new_path):
            get_all_folders(new_path, '-' + s)
        else:
            print(s, new_path)


# 49-00
def get_files0(s_path: str, ext='.pdf'):
    for dirpath, dirnames, filenames in os.walk(s_path,topdown=False):
        for filename in filenames:
            name, suf = os.path.splitext(filename)
            if suf == ext:
                print(os.path.join(dirpath, filename))

# 49-01
def get_files1(s_path: str, ext='.pdf'):
    for c_path in os.listdir(s_path):
        # print(c_path)
        new_path = os.path.join(s_path, c_path)
        if os.path.isfile(new_path):
            if c_path.endswith(ext):
                print(new_path)
        elif os.path.isdir(new_path):
            get_files1(new_path)

# 49-02
def get_files2(s_path: str, ext='.pdf'):
    for x in iglob(f'{s_path}/**/*{ext}',recursive=True):
        print(x)

if __name__ == '__main__':
    # get_all_folders('C:\\Books')
    get_files1('C:\\Books')
    print('-'*20)
    get_files2('C:\\Books')