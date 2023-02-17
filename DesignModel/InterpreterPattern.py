from abc import *


class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def Interpret(self, content: str):
        pass


class TerminalExpression(AbstractExpression):
    def Interpret(self, content: str):
        print('解释器%s解释了内容%s' % (self.__class__.__name__, content))


class NoTerminalExpression(AbstractExpression):
    def Interpret(self, content: str):
        print('解释器%s解释了内容%s' % (self.__class__.__name__, content))

if __name__=='__main__':
    te=TerminalExpression()
    nte=NoTerminalExpression()

    content='\' 需要解释的内容 \''

    te.Interpret(content)
    nte.Interpret(content)

