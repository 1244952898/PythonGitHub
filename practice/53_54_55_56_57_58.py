# 53 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
str = "k:1 |k1:2|k2:3|k3:4"
kv = {k: int(v) for s in str.split('|') for k, v in (s.split(':'),)}
print(kv)
print('-' * 50)

for s in str.split('|'):
    print(s)
    if s.endswith('1'):
        for k, v in (s.split(':'),):
            print(k, v)

print('-' * 50)
# 54 请反转字符串 "aStr"?
str = 'aStr'
print(str[::-1])

print('-' * 50)
# 55 请按alist中元素的age由大到小排序
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
lst0 = sorted(alist, key=lambda x: x['age'], reverse=True)
print(lst0)

# 56.下面代码的输出结果将是什么？
lst1 = ['a', 'b', 'c', 'd', 'e']
print(lst1[10:])

# 57.写一个列表生成式，产生一个公差为11的等差数列
lst2 = [i * 11 for i in range(10)]
print(lst2)

# 58 给定两个列表，怎么找出他们相同的元素和不同的元素？
list1 = [1, 2, 3]
list2 = [3, 4, 5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)
