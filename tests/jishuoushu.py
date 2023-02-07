
str0='1982376455'
lst=[]
for s in str0:
    lst.append(int(s))
lst.sort(reverse=True)
res=[]
print(lst)
for n in lst:
    if n%2==0:
        res.append(n)
    else:
        res.insert(0,n)
print(res)
print(''.join(str(x) for x in res))

lst1=[x*2 for x in range(4)]
print(lst1)
funcs=[lambda x:x*i for i in range(4)]
for f in funcs:
    print(f(1))