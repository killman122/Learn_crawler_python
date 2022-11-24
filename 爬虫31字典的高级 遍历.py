# 遍历:将数据一个一个输出
person = {'name': '阿玛', 'age': 18, 'sex': '男'}
# 遍历方式总有四种 在字典的定义中冒号前的叫做key也叫做key的名称 冒号后面的叫做value也叫做key的value
'''
                总共有四种遍历方式
遍历字典的key
遍历字典的value
遍历字典的key和value
遍历字典项/元素
'''
# 第一种方法 遍历字典的key 该种方法常用与多账户用户输入 也就是多账号登陆 在一次的执行中 执行多个账号的任务 例如sessionKey的遍历
# 字典.keys()方法 获取字典中所有的key值 也就是 返回了key的名字
for key in person.keys():
    print(key)
for keyvalue in person:
    print(keyvalue)

# 第二种 遍历字典的value
# 字典.values()方法  获取字典中所有的value值 其中value也是一个变量名可以随意修改
for value in person.values():
    print(value)

# 第三种 遍历字典的key和value
for key, value in person.items():
    print(key, value)

# 第四种 遍历字典项/元素
for item in person.items():
    print(item, type(item))  # 元组使用()圆括号
