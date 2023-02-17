from functools import reduce

str = '12345'


def convert_str_to_int0(ss: str) -> int:
    """
    convert string to int
    :param ss: input value
    :return: return value
    """
    num = 0
    for s in ss:
        num = num * 10 + int(s)
    print(num)
    return num


def convert_str_to_int1(ss: str) -> int:
    num = 0
    for s in ss:
        num = num * 10 + (ord(s) - ord('0'))
    print(num)
    return num


def convert_str_to_int2(ss: str) -> int:
    num = reduce(lambda a, b: a * 10 + int(b), ss, 0)
    print(num)
    return num


convert_str_to_int0(str)
convert_str_to_int1(str)
convert_str_to_int2(str)
