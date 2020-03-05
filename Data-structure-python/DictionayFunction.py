# Dictionary functions

dict = {'Name': 'Abc', 'Age': 18}
print(len(dict))
# 2

dict = {'Name': 'Abc', 'Age': 18}
print(type(dict))
# <class 'dict'>

print(str(dict))
#{'Name': 'Abc', 'Age': 18}

print(type(str(dict)))
# <class 'str'>

dict = {'Name': 'Abc', 'Age': 7}
print(len(dict))
# 2
dict.clear()
print(len(dict))
# 0

dict1 = {'Name': 'Abc', 'Age': 7}
dict2 = dict1.copy()
print(dict2)
#{'Name': 'Abc', 'Age': 7}

tupl = ('name', 'age')
dict = dict.fromkeys(tupl)
print(dict)
#{'name': None, 'age': None}

dict = dict.fromkeys(tupl, 10)
print(dict)
# {'name': 10, 'age': 10}

dict = {'Name': 'abc', 'Age': 7}
print(dict.get('Age'))
# 7

print(dict.get('Education', "Never"))
# Never

dict = {'Name': 'Abc', 'Age': 7}

print(dict.items())
# dict_items([('Name', 'Abc'), ('Age', 7)])

print(dict.values())
#dict_values(['Abc', 7])

print(dict.keys())
# dict_keys(['Name', 'Age'])

dict1 = {'Name': 'xyz', 'Age': 7}
dict2 = {'Gender': 'male'}
dict1.update(dict2)

print(dict1)
# {'Name': 'xyz', 'Age': 7, 'Gender': 'male'}
