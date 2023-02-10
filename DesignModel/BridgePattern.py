from abc import ABCMeta, abstractmethod


class Draw(metaclass=ABCMeta):
    @abstractmethod
    def DrawColor(self):
        pass


class DrawRed(Draw):
    def DrawColor(self):
        print('Draw color of %s' % self.__class__.__name__)


class DrawGreen(Draw):
    def DrawColor(self):
        print('Draw color of %s' % self.__class__.__name__)


class Square(metaclass=ABCMeta):
    @abstractmethod
    def DrawSquare(self):
        pass


class Circle(Square):
    def __init__(self, drawColor):
        self.DrawColor = drawColor

    def DrawSquare(self):
        print('draw square of %s' % self.__class__.__name__)
        self.DrawColor.DrawColor()


if __name__ == '__main__':
    dr = DrawRed()
    dg = DrawGreen()

    c = Circle(dr)
    c.DrawSquare()
    c.DrawColor = dg
    c.DrawSquare()
