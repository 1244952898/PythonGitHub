class Per:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def p(self):
        print('test')

    def __call__(self, x,y):
        self.name=x
        self.age=y
        self.p()

if __name__=='__main__':
    p0=Per('zach',11)
    print(p0.__dict__)
    p0('zz',22)
    print(p0.__dict__)