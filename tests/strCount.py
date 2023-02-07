def get_str_count(strings:str):
    dict0={}
    for s in strings:
        dict0[s]=dict0.get(s,0)+1
    return dict0
d=get_str_count('aabdfasdfawefasdfas')
print(d)
str_count=''
for k,v in d.items():
    str_count += k + str(v)
print(str_count)