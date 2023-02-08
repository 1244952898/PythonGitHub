class Target:
    def Request(self):
        print(self.__class__.__name__,'-Request')

class Adaptee():
    def SpecifictRequest(self):
        print(self.__class__.__name__,'-SpecifictRequest')

class Adapter(Target):
    def __init__(self):
        self.adaptee=Adaptee()

    def Request(self):
        self.adaptee.SpecifictRequest()


if __name__ == '__main__':
    adapter=Adapter()
    adapter.Request()