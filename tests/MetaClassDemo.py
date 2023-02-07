def meta_method(cls_name, cls_parents, cls_attrs):
    uppercase_attr = {}
    for name, val in cls_attrs.items():
        print(name, val)
        if name.startswith('__'):
            uppercase_attr[name] = val
        else:
            uppercase_attr[name.upper()] = val

    return type(cls_name, cls_parents, uppercase_attr)


class Foo(object, metaclass=meta_method):
    # __metaclass__ = meta_method
    bar = 'abc'


f = Foo()
print(dir(Foo))
print(hasattr(Foo, 'BAR'))
print(hasattr(Foo, 'bar'))


class upper_meta_class(type):
    def __new__(cls, cls_name, cls_parents, cls_attrs):
        upper_attrs = {}
        for name, val in cls_attrs.items():
            if name.startswith('__'):
                upper_attrs[name] = val
            else:
                upper_attrs[name.upper()] = val
        print('_'*90)
        return type.__new__(cls, cls_name, cls_parents, upper_attrs)

    @classmethod
    def test(mcs):
        pass
class Foo1(metaclass=upper_meta_class):
    name = 11


f1 = Foo1()
print(dir(Foo1))
print(hasattr(Foo1, 'NAME'))
print(hasattr(Foo1, 'name'))
