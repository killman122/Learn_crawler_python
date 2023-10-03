# list 列表
# tuple 元组
# dict 字典 
# 单引号是字典双引号是json字符串
# list 列表  列表使用中括号
name_list = ['周杰伦', '科比']
print(name_list,type(name_list))
print(name_list[0])
for i in name_list:
    print(i)
# 应用场景:当获取到多个数据的时候,我们将他们存储到列表中 然后使用列表访问

# tuple 元组  元组在这里使用圆括号 对于字符串类型数据使用单引号
age_tuple = (18, 11, 21)
print(age_tuple,type(age_tuple))
for i in age_tuple:
    print(i)
# dict 字典
# 应用场景:scrapy框架使用
# 格式:变量名={key:value,key1:value1}
person = {'name': '红浪漫', 'age': '19'}
print(person,type(person))

for key in person:
    print(key)
