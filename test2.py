class singleton0:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(singleton0, cls).__new__(cls, *args, **kwargs)
        return cls.instance


class s0():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(s0, cls).__new__(cls, *args, **kwargs)
        return cls.instance

class Sinleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance=super(Sinleton).__new__(cls,*args,**kwargs)
        return cls.instance