import random

print(random.randrange(1, 10))

str0 = """adfasfdas
asfdasfasfdfsadfsa
asdfasfdasfd
"""
print(str0)
st1 = "0123456789"
print(st1[-5:-1])

class class0():
    def __len__(self):
        return 1

print(bool(class0))

lst0=[0,1,2,3,4,5,6,7,8,9,0]
lst1=[11,22,33]
lst0[1:4]=lst1[0:]
print(lst0)

lst3=[0*3]