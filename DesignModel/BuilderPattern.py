
from abc import *


class PersonBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.name = 'zy'
        self.age = 20

    @abstractmethod
    def Head(self):
        pass

    @abstractmethod
    def Body(self):
        pass

    @abstractmethod
    def Arm(self):
        pass

    @abstractmethod
    def Leg(self):
        pass


class FatPersonBuilder(PersonBuilder):
    def Head(self):
        print(self.__class__.__name__, ':Head')
        return self.__class__.__name__, ':Head'

    def Body(self):
        print(self.__class__.__name__, ':Body')
        return self.__class__.__name__, ':Body'

    def Arm(self):
        print(self.__class__.__name__, ':Arm')
        return self.__class__.__name__, ':Arm'

    def Leg(self):
        print(self.__class__.__name__, ':Leg')
        return self.__class__.__name__, ':Leg'


class ThinPersonBuilder(PersonBuilder):
    def Head(self):
        print(self.__class__.__name__, ':Head')
        return self.__class__.__name__, ':Head'

    def Body(self):
        print(self.__class__.__name__, ':Body')
        return self.__class__.__name__, ':Body'

    def Arm(self):
        print(self.__class__.__name__, ':Arm')
        return self.__class__.__name__, ':Arm'

    def Leg(self):
        print(self.__class__.__name__, ':Leg')
        return self.__class__.__name__, ':Leg'

class PersonDirector():
    def __init__(self,builder:PersonBuilder):
        self.builder=builder

    def CreatePerson(self):
        print('name:',self.builder.name,'age:',self.builder.age)
        h= self.builder.Head()
        b=self.builder.Body()
        a= self.builder.Arm()
        l=self.builder.Leg()
        return Person(h,b,a,l)
class Person:
    def __init__(self,head,body,arm,leg):
        self.head=head
        self.body=body
        self.arm=arm
        self.leg=leg
    def __str__(self):
        return 'head:%s body:%s arm:%s leg:%s'%(self.head,self.body,self.arm,self.leg)
if __name__ == '__main__':
    fpBuilder=FatPersonBuilder()
    pd0 = PersonDirector(fpBuilder)
    p0= pd0.CreatePerson()
    print(p0)

    tpBuilder=ThinPersonBuilder()
    pd1=PersonDirector(tpBuilder)
    p1=pd1.CreatePerson()
    print(p1)