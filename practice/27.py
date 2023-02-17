#1.引入日志
#2.函数执行时间统计
#3.执行函数前预备处理
#4.执行函数后清理
#5.权限校验
#6.缓存
#7.事务处理
import time
from functools import wraps


def TimeDecorator(func):
    print('运行TimeDecorator')
    @wraps(func)
    def in_func(*args,**kwargs):
        t_begin=time.time()
        print('当前时间：',t_begin)
        func(*args,**kwargs)
        t_end=time.time()
        print('结束时间：', t_end)
        print('总计花费%s s时间'%(t_end-t_begin))
    return in_func

def LogDecorator(func):
    print('开始运行方法LogDecorator')
    @wraps(func)
    def inner(*args,**kwargs):
        print('纪录开始日志')
        func(*args,**kwargs)
        print('纪录结束日志')
    return inner

@TimeDecorator
@LogDecorator
def sleepMethod(n:int=2):
    print('运行本地方法开始')
    time.sleep(n)
    print('运行本地方法结束')

if __name__=='__main__':
    sleepMethod(3)

