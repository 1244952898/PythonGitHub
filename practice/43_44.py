from functools import reduce
a = [1,2,3,4,5,6,7,8,9,10]
aa=[i for i in a if i%2==1]
print(aa)

ss=[1,2,3,1024]
print(sum(ss))
print(reduce(lambda x,y:x+y,ss))