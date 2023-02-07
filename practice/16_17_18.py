# 16
question_list = [[1, 2], [3, 4], [5, 6]]

ints = [a for nums in question_list for a in nums]
print(ints)

# 17
# 字典类型中的键必须是不可变类型，可变类型list dict set不能作为键
# 一个对象能否作为dict的键，取决于该对象是否有hash()方法

# 18
ds = {'a': 1, 'b': 2}
ds0 = {v: k for k, v in ds.items()}
print(ds0)
