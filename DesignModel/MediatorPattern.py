from abc import *


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def Send(self, message: str, colleague):
        pass


class Colleague(metaclass=ABCMeta):
    def __init__(self, mediator):
        self.mediator = mediator


class ConcreteColleagueA(Colleague):
    def Send(self, msg):
        self.mediator.Send(msg, self)

    def Receive(self, msg):
        print('Receive msg: %s' % msg)


class ConcreteColleagueB(Colleague):
    def Send(self, msg):
        self.mediator.Send(msg, self)

    def Receive(self, msg):
        print('Receive msg: %s' % msg)


class ConcreteMediator(Mediator):
    def __init__(self):
        self.ColleagueA = None
        self.ColleagueB = None

    def Send(self, message: str, colleague):
        if not self.ColleagueA or not self.ColleagueB:
            print('give self.ColleagueA and self.ColleagueB')
            return
        if type(colleague) == ConcreteColleagueA:
            self.ColleagueB.Receive(message)
        else:
            self.ColleagueA.Receive(message)


if __name__ == '__main__':
    m = ConcreteMediator()

    cca = ConcreteColleagueA(m)
    ccb = ConcreteColleagueB(m)

    cca.Send('123')

    m.ColleagueA = cca
    m.ColleagueB = ccb
    cca.Send('234')
    ccb.Send('345')
