# python中通过json模块来实现对数据的序列化与反序列化
# 序列化定义:按照某种规则,将内存中的二数据转换为字节序列,并保存到文件中,这即为序列化
# 反序列化定义:从文件中的字节序列恢复到内存中,就是反序列化
# 应用场景在使用scrapy框架的时候 该框架会返回一个对象 我们要将对象写入到文件中 则要使用json.dumps()

'''
对象-->字节序列==序列化
字节序列-->对象==反序列化
'''
'''
fp=open('text.txt','w')
#默认情况下我们只能将字符串写入到文件中 换言之在将数据写入后数据类型变为字符串类型数据
fp.write('hello world')
fp.close()
'''
'''
#在将非字符串类型的数据写入指定的文件中时比如列表此时会报错  write() argument must be str, not list
fp=open('text.txt','w')
#默认情况下 对象是无法写入到文件中的 如果想写入到文件那么必须使用序列化操作
name_list=['张三','里斯']
fp.write(name_list)
fp.close()
'''
# 序列化的两种方式
# dumps()
# (1)创建一个文件
f = open('text.txt', 'w')
# (2)定义一个列表
name_list = ['张三', '里斯']
# (3)导入json模块到该文件中
import json

# (4)序列化
# 将python 对象 变为json字符串 也就是将不带有unicode码的数据变为带有unicode码的数据

names = json.dumps(name_list)  # 转换为json字符串后使用了unicode加密保存字符串
print(names)
print(type(names))
# (5)当发现数据已经改变成为 str类型的数据时 数据可以存入文件中 因为文件中只允许存入str字符串类型的变量
f.write(names)
# f.write(json.dumps(name_list))
f.close()

# dump --将对象转换为字符串的同时指定一个文件的对象 然后将转换后的字符串写入到那个文件中--意思就是将数据直接转换为json字符串后导入到指定的文件中不需要上诉的两步操作
f = open('test.txt', 'w')
json.dump(name_list, f)  # --这里的对象指的就是目标 name_list fp=f
f.close()

'''
反序列化
将json字符串变为 一个python对象 就像是上面的将python对象列表转换为字符串数据存到json字符串中这是指序列化,反序列化与之相反,将json字符串中的数据转换为 列表文件 

反序列化的两种方法 loads和load
'''
fp = open('test.txt', 'r')

content = fp.read()  # --在此处若使用readlines则输出的列表类型数据 但是如果是read()的单个字节读取 则显示为str字符串类型
# content=fp.readlines()
# 将json字符串变为python对象
# json.loads(content)
result = json.loads(content)
print(content, type(content))  # 转换之前,这里输出的依然是未转换为转换为json格式仍为字符串的content
print(result, type(result))  # 转换之后

# ----注意----
# 上面的反序列化的方法在json数据的返回,也就是获取到一个参数随着请求体返回,此时需要将json数据反序列化用来保存数据或者传递参数到另一个接口上

# 下面的时第二种方法load()这种方法可以参考前面的dump()直接使用json的接口,不需要在将数据读取后在进行操作,也就是将数据直接进行反序列化,将json字符串转换为原本的python对象
f = open('text.txt', 'r')
result1 = json.load(f)
print(result1, type(result1))



"""
注意此方法JavaScript中的特有方法不要将语言之间的方法使用混乱

使用JSON.parse()方法能够将一个字符串,字符串中包含类似字典的结构,这里的字典貌似算一个对象,通过JSON.parse()方法将字符串转换为json对象

使用JSON.stringify()将json对象转换为json字符串也就是一般的字符串
"""
