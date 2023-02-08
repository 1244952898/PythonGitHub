from abc import ABCMeta,abstractmethod

class Context:
    def __init__(self,state):
        self.state=state
    def Request(self):
        self.state.Handle(self)

class State(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self,context:Context):
        pass

class ConcreteStateA(State):
    def Handle(self,context:Context):
        print(self.__class__.__name__)
        context.state=ConcreteStateB()

class ConcreteStateB(State):
    def Handle(self,context:Context):
        print(self.__class__.__name__)
        context.state = ConcreteStateA()


if __name__ == '__main__':
    ca=ConcreteStateA()
    cb=ConcreteStateB()

    c=Context(ca)
    c.Request()
    c.Request()
    c.Request()

