import sys


class iterandnext():
    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        x = self.i
        self.i += 1
        if x > 3:
            raise StopIteration
        return self.nums[x]


nums = ['a', 'b', 'c', 'd', 'e']
ian = iterandnext(nums)
iian = iter(ian)
print('next is %s'%next(iian))
print('next is %s'%next(iian))
for x in iian:
    print(x)
#
# class fibonacciDemo():
#     def fibonacci(self,n):
#         a,b,count=0,1,0
#         while True:
#             if count>n:
#                 break
#             yield a
#             a,b=b,b+a
#             count+=1
#     def exec(self):
#         f=self.fibonacci(10)
#         while True:
#             try:
#                 print(next(f),end=' ')
#             except StopIteration:
#                 sys.exit()
# f=fibonacciDemo()
# f.exec()

def printinfo(a,b,c,*d,**e):
    print("输出: ")
    print(a,b,c)
    print(d)
    print(*d)
    print(e)
# printinfo(1,2,3,4,5,6,7,8,9,x=1,y=2,z=3)
printinfo(1,2,3,4,5,6,7,8,9, **{'x' : 1, 'y' : 2, 'z' : 3})
class JustCounter:
    __secretCount = 0  # 私有变量
    a=10
    def test(self):
        print(JustCounter.a)
        a=20
        print(a)
j=JustCounter()
print(dir(j))
print(dir(JustCounter))
j.test()
