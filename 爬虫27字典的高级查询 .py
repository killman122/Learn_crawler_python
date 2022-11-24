# 定义一个字典
person = {'name': '吴倩', 'age': 28}
# 访问person的name
# 字典中的数据使用[]访问,其中[]内加入key值 这里与json数据中的返回json字符串中的方法使用一致
print(person['name'])  # 这里如果是返回了多个括号包含的数据多在json数据中需要使用多个变量多次保存,先保存最大括号的父变量
print(person['age'])
# 在使用从字典中对数据的查询或者保存时,必须要将其中的方括号输入还有其中的单引号


# 当在获取字典中不存在的key的数据值时,会报错在运行后
# print(person['a'])
'''
不能使用.的方式访问数据
当使用字典名.对象的时候会发生错误:
'dict' object has no attribute 'name'
'''

# 在使用get 的方式获取数据时 可以与使用方括号['']的访问起到相同的作用
# 但是在使用get的方式访问不存在的键值时不会产生错误但是会返回NOne的空值
a = person.get('name')
print(a)
print(person.get('age'))
