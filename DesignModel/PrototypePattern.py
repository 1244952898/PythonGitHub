import copy
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    _id = ''
    name = ''

    @abstractmethod
    def clone(self):
        pass

    def getID(self):
        return self._id

    def setID(self,id):
        self._id=id

    def getName(self):
        return self.name


class ConcretePrototype(Prototype):

    def clone(self):
        clone = copy.deepcopy(self)
        return clone


if __name__ == '__main__':
    cp=ConcretePrototype()
    cp.setID(0)
    cp.name='zy'

    cp_clone=cp.clone()
    print(cp_clone.getID(),cp_clone.name)
