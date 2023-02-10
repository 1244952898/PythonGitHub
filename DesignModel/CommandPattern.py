from abc import *
class Reciever:
    def ActionA(self):
        print('命令接受者执行命令A')

    def ActionB(self):
        print('命令接受者执行命令B')

class Command(metaclass=ABCMeta):

    def __init__(self,reciever):
        self.reciever=reciever

    def SetCommand(self,reciever):
        self.reciever=reciever

    @abstractmethod
    def ExcuteCommand(self):
        pass

class ConcreteCommandA(Command):
    def ExcuteCommand(self):
        self.reciever.ActionA()

class ConcreteCommandB(Command):
    def ExcuteCommand(self):
        self.reciever.ActionB()

class Invoker():
    __commands=[]

    def SetCommand(self,command):
        self.__commands.append(command)
    def Excute(self):
        for c in self.__commands:
            c.ExcuteCommand()

if __name__ == '__main__':
    r=Reciever();
    ca=ConcreteCommandA(r)
    cb=ConcreteCommandB(r)

    i=Invoker()
    i.SetCommand(ca)
    i.SetCommand(cb)

    i.Excute()


