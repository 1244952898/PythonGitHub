class Originator:
    def __init__(self):
        self.state='state_a'
        self.name='zy'
    def getMemento(self):
        m=Memento(self.state)
        return m
    def setMemento(self,me):
        self.state=me.state
    def __str__(self):
        return '%s-%s'%(self.name,self.state)

class Memento:
    def __init__(self,state):
        self.state=state

class CareTaker:
    def __init__(self):
        self.memento=None

if __name__ == '__main__':
    o=Originator()
    m=o.getMemento()

    c=CareTaker()
    c.memento=m

    print(o)
    o.name='zy1'
    o.state='state_b'
    print(o)
    o.setMemento(m)
    print(o)