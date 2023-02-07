# Subject
# RealSubject
# Proxy
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print('method:',self.__class__.__name__)

class Proxy(Subject):
    def __init__(self,s:Subject):
        self.subject=s
    def request(self):
        print('m:',self.__class__.__name__)
        self.subject.request()

if __name__ == '__main__':
    rs=RealSubject()
    p=Proxy(rs)
    p.request()