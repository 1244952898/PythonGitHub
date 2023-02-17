import json

# 23 json序列化时，可以处理列表、字典、字符、数值、布尔和None 定制datetime类型
# 24 print(json.dumps(dict_demo, ensure_ascii=False))
person = {'name': 'zy', 'age': 35, 'gender': '男'}
json_person = json.dumps(person, ensure_ascii=False)
print(json_person)
p = json.loads(json_person)
print(p)


class Pers:
    def __init__(self):
        self.n = 'name'
        self.a = 35
        self.g = '男'


pers = Pers()
object_p = json.dumps(pers.__dict__, ensure_ascii=False)
print(object_p)


def convertPersToDict(p: Pers):
    return {'n': p.n, 'a': p.a, 'g': p.g}


o_p = json.dumps(pers, default=convertPersToDict, ensure_ascii=False)
print(o_p)


def convertDictToPer(dic: dict):
    p1 = Pers()
    p1.n = dic['n']
    p1.a = dic['a']
    p1.g = dic['g']
    return p1


p0 = json.loads('{"n": "name", "a": 35, "g": "那么"}', object_hook=convertDictToPer)
print(p0, p0.g)
