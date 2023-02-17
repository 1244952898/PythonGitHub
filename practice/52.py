items={'a':1,'b':3,'e':6,'d':4,'c':2}
items1=sorted(items.items(),key=lambda x:x[1])
print(items1)

items2=sorted(items.items())
print(items2)