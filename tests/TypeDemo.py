Person = type('Person', (object,), {'name': 'zach', 'age': 33})

p = Person()
print(p)
print(type(p))
print(p.name, p.age)
print(type(Person))
print(type(p))
print(isinstance(Person,type))