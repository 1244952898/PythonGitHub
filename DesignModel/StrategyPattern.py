from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def AlgorithmInterface(self):
        pass


class ConcreteStrategyMethodA(Strategy):
    def AlgorithmInterface(self):
        print('this is method', self.__class__.__name__)


class ConcreteStrategyMethodB(Strategy):
    def AlgorithmInterface(self):
        print('this is method', self.__class__.__name__)

class ConcreteStrategyMethodC(Strategy):
    def AlgorithmInterface(self):
        print('this is method', self.__class__.__name__)

class Context:
    def __init__(self,strategy:Strategy):
        self.strategy=strategy

    def ContextInterface(self):
        self.strategy.AlgorithmInterface()

if __name__ == '__main__':
    ca=ConcreteStrategyMethodA()
    c = Context(ca)
    c.ContextInterface()

    cb=ConcreteStrategyMethodB()
    c = Context(cb)
    c.ContextInterface()

    cc=ConcreteStrategyMethodC()
    c = Context(cc)
    c.ContextInterface()

