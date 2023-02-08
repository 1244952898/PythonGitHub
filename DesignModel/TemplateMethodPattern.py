from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):
    @abstractmethod
    def Method0(self):
        pass

    @abstractmethod
    def Method1(self):
        pass

    def method(self):
        print('步骤0')
        self.Method0()
        print('步骤2')
        self.Method1()


class ConcreteTempalte0(Template):

    def Method0(self):
        print('步骤1:', self.__class__.__name__)

    def Method1(self):
        print('步骤3:', self.__class__.__name__)


class ConcreteTempalte1(Template):

    def Method0(self):
        print('步骤1:', self.__class__.__name__)

    def Method1(self):
        print('步骤3:', self.__class__.__name__)


if __name__ == '__main__':
    print('================')
    ct0 = ConcreteTempalte0()
    ct0.method()
    print('================')
    ct1 = ConcreteTempalte1()
    ct1.method()
