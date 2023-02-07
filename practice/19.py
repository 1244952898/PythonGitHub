import sys

# 迭代器有两个基本的方法：iter() 和 next()。
lst0 = [1, 2, 3, 4]
it0 = iter(lst0)
for i in it0:
    print(i)

print('===================')
it1=iter(lst0)
while True:
    try:
        print(next(it1))
    except StopIteration as e:
        print(e)
        break

print('===================')
class my_number:
    def __iter__(self):
        self.i=4
        return self

    def __next__(self):
        a=self.i
        self.i+=1
        return a

mn=my_number()
it2=iter(mn)
print(next(it2))
print(next(it2))

print('===================')
class my_num1:
    def __iter__(self):
        self.a=10
        return self
    def __next__(self):
        b=self.a
        if b<13:
            self.a+=1
            return b
        else:
            raise StopIteration()
mn1=my_num1()
it3=iter(mn1)
for x in it3:
    print(x)

print('===================')
def fibonacci(n:int):
    i,j,counter=0,1,0
    while counter<n:
        yield i
        i,j=j,i+j
        counter+=1
    raise StopIteration
for x in fibonacci(6):
    print(x)