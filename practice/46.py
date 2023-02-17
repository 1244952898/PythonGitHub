def get_numbers(lst:list,target:int)->list:
    """

    :param lst:
    :param target:
    :return:
    """
    for l in lst:
        if target-l in lst and l is not target-l:
            return [lst.index(l),lst.index(target-l)]

nums_all = [2, 7, 11, 15]
target = 17
nums = get_numbers(nums_all, target)
print(nums)