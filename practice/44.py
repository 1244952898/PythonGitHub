#函数的作用于LEGB
#L:local 函数内部作用域,暂时的存在，依赖于创建该局部作用域的函数。函数存，则局部变量存，函数亡，则局部变量亡。
#E:enclosing 函数内部与内嵌函数之前，一般是在函数中嵌套函数的时候，外层函数的变量作用域。
#G:global 全局作用域，一般模块文件顶层声明的变量具有全局作用域，从外部来看，模块的全局变量就是一个模块对象的属性，仅限于单个模块文件中。
#B:build-in 内置作用域,解释器内置的变量，比如int, str等。

def local():
    """
    L:local 函数内部作用域
    :return:
    """
    a=1
    print(a)
local()

def enclosing0():
    """
    E:enclosing 函数内部与内嵌函数之前
    :return:
    """
    a=1
    print('enclosing0:{}'.format(a))
    def enclosing1():
        print('enclosing1:{}'.format(a))
    return enclosing1
e=enclosing0()
e()

g0=1
def global0():
    """
    G:global 全局作用域
    :return:
    """
    print('global0 :%s'%g0)
global0()