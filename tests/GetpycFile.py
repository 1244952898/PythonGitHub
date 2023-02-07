import os
from glob import iglob


def GetSuffixFiles(sPath, suffix):
    res = []
    for root, dirs, files in os.walk(sPath):
        for file_name in files:
            name, suf = os.path.splitext(file_name)
            if suf == suffix:
                res.append(os.path.join(root, file_name))
    print(res)


def GetSuffixFiles1(sPath, suffix='.pdf'):
    res = []
    for c_child in os.listdir(sPath):
        s_child = os.path.join(sPath, c_child)
        if os.path.isfile(s_child) and s_child.endswith(suffix):
            res.append(s_child)
        elif os.path.isdir(s_child):
            rs = GetSuffixFiles1(s_child)
            res.extend(rs)
    return res
def GetSuffixFiles2(sPath, suffix='.pdf'):
    for i in iglob(f'{sPath}/**/*{suffix}',recursive=True):
        print(i)



if __name__ == '__main__':
    url = 'C:\SoftwareDownload\94-DDD实战课'
    GetSuffixFiles(url, '.pdf')

    ps = GetSuffixFiles1(url, '.pdf')
    print(ps)

    ps = GetSuffixFiles2(url, '.pdf')