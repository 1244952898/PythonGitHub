class A:
    def m(self):
        print('A.m()')


class B(A):
    def m(self):
        print('B.m()')


class C(A):
    def m(self):
        print('C.m()')


class D(C, B):
    def m(self):
        print('D.m()')


class E(D):
    def m(self):
        print('E.m()')


class F(C):
    def m(self):
        print('F.m()')


class G(E, F):
    def m(self):
        super().m()


print(G.__mro__)
g=G()
g.m()

class AA:
    def m(self):
        print('AA.m()')
        super().m()
class BB:
    def m(self):
        print('BB.m()')
class CC(AA,BB):
    pass
cc=CC()
cc.m()