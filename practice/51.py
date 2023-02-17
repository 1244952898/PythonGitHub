#51.打乱一个排好序的list对象alist
import random

lst=[1,2,3,4,5,6]
random.shuffle(lst)
print(lst)

lst1=[1,2,3,4,5,6]
lst2=list(lst1)
for i in range(len(lst1)):
    lst1[i]=lst2.pop(random.randrange(len(lst2)))
print(lst1)
