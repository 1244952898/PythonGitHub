import os.path
import re


def get_max_words(path: str):
    distone = {}
    with open(path, 'r') as f:
        for line in f:
            line = re.sub('\W', '', line)
            words = line.split()
            for w in words:
                if w in distone:
                    distone[w] += 1
                else:
                    distone[w] = 1

    numTen = sorted(distone.items(), key=lambda x: x[1], reverse=True)[:10]
    ns = [x[0] for x in numTen]
    print(ns)


if __name__ == '__main__':
    p = os.path.join('../', 'files/59.txt')
    # path = os.path.join('../', 'files/file.txt')
    get_max_words(p)
