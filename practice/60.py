def ger(s):
    l=[]
    if isinstance(s,str):
        l=[int(i) for i in s]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i]%2==1:
            n=l.pop(i)
            l.insert(0,n)
    print(l)

if __name__=='__main__':
    ger('1982376455')
