from abc import *


class Element(metaclass=ABCMeta):
    @abstractmethod
    def Accept(self, visitor):
        pass


class ConcreteElementA(Element):
    def Accept(self, visitor):
        visitor.VisitConcreteElementA(self)

    def OperationA(self):
        print('OperationA')


class ConcreteElementB(Element):
    def Accept(self, visitor):
        visitor.VisitConcreteElementB(self)

    def OperationB(self):
        print('OperationB')


class Visitor:
    @abstractmethod
    def VisitConcreteElementA(self, concreteElementA: ConcreteElementA):
        pass

    @abstractmethod
    def VisitConcreteElementB(self, concreteElementB: ConcreteElementB):
        pass


class ConcreteVisitor1(Visitor):
    def VisitConcreteElementA(self, concreteElementA: ConcreteElementA):
        print('%s被%s访问' % (concreteElementA.__class__.__name__, self.__class__.__name__))

    def VisitConcreteElementB(self, concreteElementB: ConcreteElementB):
        print('%s被%s访问' % (concreteElementB.__class__.__name__, self.__class__.__name__))

class ConcreteVisitor2(Visitor):
    def VisitConcreteElementA(self, concreteElementA: ConcreteElementA):
        print('%s被%s访问' % (concreteElementA.__class__.__name__, self.__class__.__name__))

    def VisitConcreteElementB(self, concreteElementB: ConcreteElementB):
        print('%s被%s访问' % (concreteElementB.__class__.__name__, self.__class__.__name__))

class ObjectStructure():
    def __init__(self):
        self.Elements=[]

    def Add(self,ele):
        self.Elements.append(ele)

    def Remove(self,ele):
        self.Elements.remove(ele)

    def Accept(self,visitor):
        # print(len(self.Elements))
        # print(self.Elements)
        for e in self.Elements:
            e.Accept(visitor)

if __name__ == '__main__':
    objectStructure=ObjectStructure()

    cca=ConcreteElementA()
    ccb=ConcreteElementB()
    objectStructure.Add(cca)
    objectStructure.Add(ccb)

    cv1=ConcreteVisitor1()
    cv2=ConcreteVisitor2()
    objectStructure.Accept(cv1)
    objectStructure.Accept(cv2)
