import re


def get_top_word(spath: str, top: int):
    distone = {}
    with open(spath, mode='r', encoding='utf-8') as f:
        for line in f:
            #print(line)
            line = re.sub("\W", "", line)
            #line_one = line.split()
            #print(line_one)
            for key_one in line:
                print(key_one)
                if key_one in distone.keys():
                    distone[key_one] += 1
                else:
                    distone[key_one] = 1
    lst0 = sorted(distone.items(),key= lambda x: x[1], reverse=True)
    print(distone)
    print(lst0)
    lst0 = lst0[:10]
    res = [x[0] for x in lst0]
    print('-'*100)
    print(res)


if __name__ == '__main__':
    get_top_word(f'C:\\Projects\\Pythods\\1.txt', 10)
