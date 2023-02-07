import sys
from abc import abstractmethod, ABCMeta


class Abstract_Base(metaclass=ABCMeta):
    @abstractmethod
    def m0(self):
        print('Abstract_Base:m0')

    @abstractmethod
    def m1(self):
        print('Abstract_Base:m1')


class impl_abstract(Abstract_Base):

    def m0(self):
        print('Impl_Abstract:mo')


impM = impl_abstract()
impM.m0()
impM.m1()
