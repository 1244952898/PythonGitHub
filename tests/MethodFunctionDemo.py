from types import FunctionType, MethodType


class MethodFunctionDemo:
    def demo(self):
        print('MethodFunctionDemo')

    @staticmethod
    def static_demo(self):
        print('staticmethod')


mf = MethodFunctionDemo()
print(isinstance(MethodFunctionDemo.demo, FunctionType))
print(isinstance(MethodFunctionDemo.demo, MethodType))
print(isinstance(mf.demo, FunctionType))
print(isinstance(mf.demo, MethodType))

print(isinstance(MethodFunctionDemo.static_demo, FunctionType))
print(isinstance(MethodFunctionDemo.static_demo, MethodType))
print(isinstance(mf.static_demo, FunctionType))
print(isinstance(mf.static_demo, MethodType))
