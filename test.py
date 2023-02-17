import random

lst0=[1,2,3,4,5,6,7]
lst1=lst0[:]
for i in range(len(lst0)):
    lst1[i]=lst0.pop(random.randrange(0,len(lst0)))
print(lst1)

lst2=[1,2,3,4,5,6,7]
random.shuffle(lst2)
print(lst2)

s='ww aa bb cc dd ee ffgg'
for a in s.split():
    print(a)

set0={'a':1,'b':2,'c':3}
print('a' in set0)