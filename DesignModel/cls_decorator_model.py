class Decorator():
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        print('before----')
        res = self.func( *args, **kwargs)
        print('after----')
        return res
@Decorator
def add(a:int,b:int)->int:
    print(111)
    return a+b
print(add(1,3))
#
# print('-'*100)
# import time
# class Decorator:
#     def __init__(self, func):
#         self.func = func
#
#     def defer_time(self):
#         time.sleep(5)
#         print("延时结束了")
#
#     def __call__(self, *args, **kwargs):
#         self.defer_time()
#         self.func()
#
#
# @Decorator
# def f1():
#     print("延时之后我才开始执行")
# f1()