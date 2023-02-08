from abc import ABCMeta, abstractmethod

class Subscribe(metaclass=ABCMeta):
    @abstractmethod
    def Update(self):
        pass

class ConcreteSubscribe0(Subscribe):
    def Update(self):
        print(self.__class__.__name__)


class ConcreteSubscribe1(Subscribe):
    def Update(self):
        print(self.__class__.__name__)

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def Add(self,s:Subscribe):
        pass

    @abstractmethod
    def Remove(self,s:Subscribe):
        pass

    @abstractmethod
    def Notify(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self.subscribes=[]

    def Add(self, s: Subscribe):
        self.subscribes.append(s)

    def Remove(self,s:Subscribe):
        self.subscribes.remove(s)

    def Notify(self):
        print('ConcreteSubject run Notify')
        for s in self.subscribes:
            # print(dir(s))
            s.Update()

if __name__ == '__main__':
    c0=ConcreteSubscribe0()
    c1=ConcreteSubscribe1()

    s=ConcreteSubject()
    s.Add(c0)
    s.Add(c1)
    s.Notify()