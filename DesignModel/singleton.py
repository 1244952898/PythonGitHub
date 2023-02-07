def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Foo():
    pass


class Singleton1():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance111'):
            cls._instance111 = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instance111


class Foo1(Singleton1):
    pass


if __name__ == '__main__':
    f0 = Foo()
    f1 = Foo()
    print(f0, f1, f0 is f1)

    f00 = Foo1()
    f01 = Foo1()
    print(f00, f01, f00 is f01)
