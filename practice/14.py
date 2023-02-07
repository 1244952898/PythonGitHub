import re

s="info：xiaoZhang 33 shandong"
strs = re.compile('\W').split(s)
print(strs)

ss='a1b2c3dde4f'
strs0=re.compile('\d').split(ss)
print(strs0)