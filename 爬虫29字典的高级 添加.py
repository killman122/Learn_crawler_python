person = {'name': '老马'}
print(person['name'])  # 这里不能忘记加入字典的名称否则输出的不是想要的元素
# 给字典添加一个新的key value
# 如果使用变量名字['键']=数据时  这个键如果在字典中不存在  那么就会变成新增元素
# 如果这个键在字典中已经存在那么进行上述操作就变成了修改字典中的键值
# print={'name':'老张'}
person['age'] = 18
print(person)
# 再写入的语句不完全是运行会报错 原因是没有输出的条件 只有运行的函数
