def verify_permissions(func):
    def wapper(*args, **kwargs):
        print('权限验证')
        func(*args, **kwargs)

    return wapper


def verify_permissions1(func):
    def wapper(*args, **kwargs):
        print('添加参数')
        args = args+(3,)
        print(args)
        func(*args, **kwargs)

    return wapper


@verify_permissions
def del_order(a, b):
    """

    :return:
    """
    print('删除订单')


@verify_permissions
def enter_order(id):
    """

    :return:
    """
    print('进入后台%s' % id)


@verify_permissions1
def printArgs(*args):
    print(args)


# enter_order=verify_permissions(enter_order)
# del_order=verify_permissions(del_order)
enter_order(1)
del_order(1, 2)

print(123E2)
printArgs(1,2)