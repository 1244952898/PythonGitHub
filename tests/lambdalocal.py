def func():
    lambdaFunc=[]
    for i in range(4):
        def lf(x):
            print('Lambda函数中 i {} 命名空间为：{}:'.format(i, locals()))
            return x*i
        lambdaFunc.append(lf)
        print('外层函数 I 为：{} 命名空间为:{}'.format(i, locals()))
    return lambdaFunc
fs=func()
for f in fs:
    f(1)
