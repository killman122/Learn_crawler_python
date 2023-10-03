# 删除在python中共有两种方式 一种是del 指的是delete 另一种是cle 指的是clear
'''
del
删除字典中指定的某一个元素
删除整个字典

clear
清空字典但是保留了字典对象
'''
# 使用del删除的案例
# 使用del删除是删除指定字典中的指定项 并且删除了指定项的整个字典这里与clear不同 并且删除的时候必须要使用del 字典名['key名']
person = {'name': '老马', 'age': 19}
# 删除之前
print(person)
del person['age']
print(person)
# 如果要删除整个字典 那么就要使用del 字典名 后面无需加key的名称 如此删除会导致整个字典删除掉 如果在后面使用print 打印的时候就会报错
print(person)
del person
# print(person)

# 使用cle删除的案例
# 使用cle删除是后面不能加参数在括号内 但是保留了字典的结构{}
person = {'name': '老马', 'age': 19}
print(person)
person.clear()
print(person, type(person))
