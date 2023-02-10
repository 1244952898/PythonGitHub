from abc import *
class Componment(metaclass=ABCMeta):
    def __init__(self):
        self.name=''
    @abstractmethod
    def Add(self,c):
        pass

    @abstractmethod
    def Remove(self,c):
        pass

    @abstractmethod
    def Display(self,s):
        pass
class Leaf(Componment):
    def __init__(self,name):
        self.name=name

    def Add(self,c):
        print('Cannot add ',self.__class__.__name__,'-Add')

    def Remove(self,c):
        print('Cannot remove ',self.__class__.__name__,'-Remove')

    def Display(self,s):
        print ('%s %s'%(s,self.name))

class Composite(Componment):
    def __init__(self,name):
        self.leafs=[]
        self.name=name

    def Add(self,c):
        self.leafs.append(c)
        print(len(self.leafs))

    def Remove(self,c):
        self.leafs.remove(c)

    def Display(self, s):
        print('%s %s' % (s, self.name))
        for l in self.leafs:
            l.Display(s+'-')

if __name__ == '__main__':
    root=Composite('root')
    la=Leaf('leafA')
    lb=Leaf('leafB')
    root.Add(la)
    root.Add(lb)

    lc = Leaf('leafC')
    ld = Leaf('leafD')
    cp=Composite('Composite')
    cp.Add(lc)
    cp.Add(ld)
    root.Add(cp)

    root.Display('-')

