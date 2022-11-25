def verify_permissions(func):
    def wapper(*args, **kwargs):
        print('权限验证')
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


# enter_order=verify_permissions(enter_order)
# del_order=verify_permissions(del_order)
enter_order(1)
del_order(1, 2)
x = 10
print(type(x))
x = 'abc'
print(type(x))
z = -49.8e100
print(z)
print(123E2)
