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

lst0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lst1 = [11, 22, 33]
lst0[1:4] = lst1[0:]
print(lst0)

lst3 = [0 * 3]
str1 = '/note/test_cache'
print(str1.startswith('/note'))

rd = random.randint(0, 4)
match rd:
    case 1:
        print('match is %d' % rd)
    case 2:
        print('match is %d' % rd)
    case 3:
        print('match is %d' % rd)
    case _:
        print('match is %d' % rd)
while rd < 3:
    print('while is %d' % rd)
    rd = random.randint(0, 4)
else:
    print('while else is %d' % rd)

int0,int1=1,2
int0,int1=int1,int1+int0
print(int0,int1)
int00,int11=11,22
int11,int00=int11+int00,int11
print(int00,int11)

a = [1,2,3,None,(),[],]
print(a)
print(len(a))