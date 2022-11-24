# 当在爬虫时大部分获取的都是字符串类型的

a = '12.34'
print(type(a))
# 将字符串类型的数据转换为浮点数
b = float(a)
print(b, type(b))

a = 666
print(a, type(a))
b = float(a)
print(b, type(b))
