from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    @abstractmethod
    def OperationMethod(self):
        pass


class ConcreteComponent(Component):
    def OperationMethod(self):
        print('running class method :', self.__class__.__name__)


class DecoratePattern(Component):
    def __init__(self):
        self.com = None

    def set_component(self, com: Component):
        self.com = com

    def OperationMethod(self):
        if self.com:
            self.com.OperationMethod()

class DecoratePatternA(DecoratePattern):
    def OperationMethod(self):
        self.com.OperationMethod()
        print('running class method :', self.__class__.__name__)

class DecoratePatternB(DecoratePattern):
    def OperationMethod(self):
        print('running class method before:', self.__class__.__name__)
        self.com.OperationMethod()
        print('running class method after:', self.__class__.__name__)

class DecoratePatternC(DecoratePattern):
    def OperationMethod(self):
        self.com.OperationMethod()
        print('running class method :', self.__class__.__name__)

if __name__ == '__main__':
    concrete_component=ConcreteComponent()
    da=DecoratePatternA()
    db=DecoratePatternB()
    dc=DecoratePatternC()

    da.set_component(concrete_component)
    db.set_component(da)
    dc.set_component(db)

    dc.OperationMethod()


