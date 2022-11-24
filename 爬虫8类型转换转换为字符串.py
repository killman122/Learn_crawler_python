# 在做字符串拼接的项目中时,一定要使用 转换为字符串类型数据
# 例如同一网址不同网页之间,通过后缀的编号进行区分,但是必须转换为字符串不可以直接添加在后面
# 大部分情况下将整型转为字符串
# 强制类型转换为字符串的方法是str()不是string
# 整数转换为字符串
a = 800
print(type(a))
b = str(a)
print(b, type(b))
# string类型变量在控制台输出是可能不加引号的

# 将浮点型数据强制类型转换为字符串
a = 1.22
print(type(a))
b = str(a)
print(b, type(b))

# 布尔类型转换为字符串
a = True
print(type(a))
b = str(a)
print(b, type(b))  # 显示出的是字符串True
