class CallDemo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # print(self)

    def __call__(self, a, b):
        self.a = a
        self.b = b
        # print(self)

    def __str__(self):
        return f'${self.a}-${self.b}-${self.c}'

callDemo=CallDemo(1,2,3)
print(callDemo)
callDemo(4,5)
print(callDemo)