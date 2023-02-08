from abc import *
class SubSystem0():
    def Method(self):
        print(self.__class__.__name__)

class SubSystem1():
    def Method(self):
        print(self.__class__.__name__)

class SubSystem2():
    def Method(self):
        print(self.__class__.__name__)

class Facade():
    def __init__(self,m0:SubSystem0,m1:SubSystem1,m2:SubSystem2):
        self.m0=m0
        self.m1=m1
        self.m2=m2
    def Method0(self):
        print('使用方法Method0:',self.__dir__())
        self.m0.Method()
        self.m1.Method()
        self.m2.Method()

    def Method1(self):
        print('使用方法Method1:', self.__dir__())
        self.m0.Method()
        print('自己步骤逻辑')
        self.m2.Method()

if __name__ == '__main__':
    s0=SubSystem0()
    s1=SubSystem1()
    s2=SubSystem2()

    f=Facade(s0,s1,s2)
    f.Method0()
    f.Method1()