a = 1
print(type(a))

b = bool(a)
print(b, type(b))

c = 2
print(type(c))
d = bool(c)
print(d, type(d))

e = 0
print(type(e))
f = bool(e)
print(f, type(f))

a = -1
print(a, type(a))
b = bool(a)
print(b, type(b))

# 如果对非零的整数进行bool类型转换则全都是true,其中包括了正数和负数
# 如果是零的整数进行bool类型数据转换则是flase其中只有0

# 浮点数
a = 1.1
print(a, type(a))
b = bool(a)
print(b, type(b))

a = -1.2
print(a, type(a))
b = bool(a)
print(b, type(b))

c = 0.0
print(type(c))
a = bool(c)
print(a, type(a))

# 浮点数的bool类型转换与整数转换的一致

# 字符串
# 字符串转换为bool类型的就是true但是如果字符串是空的或者没有填满,那么字符串转换为bool类型的就是flase
# 只要字符串中有数据那么转换为bool类型后必然是true的结果但是如果字符串为空那么就是flase输出
# 此处字符串使用单引号或是双引号都一样
a = '网红聊天截图'
print(a, type(a))
b = bool(a)
print(b, type(b))

a = ''
print(type(a))
b = bool(a)
print(b, type(b))

# 列表:感觉列表更像是数组
a = ['吴亦凡', '鹿晗那', '低价', '盖亚']
print(a, type(a))
b = bool(a)
print(b, type(b))
# 若列表中含有内容则该列表在转换为bool类型变量后是一个true的结果,反之同上若列表中为空 则在列表转换为flase与上面所讲的完全一致
a = []
print(type(a))
b = bool(a)
print(b, type(b))
# 有内容极为true反之flase


# 元组
# 元组也是同上,只要存在数据的输入那么数据转换为bool类型数据后都是变为true 反之如果为flase则是数据为空
a = ('李逵', '潘金莲', '武松', '卢俊义')
print(a, type(a))

b = bool(a)
print(b, type(b))

a = ()
print(a, type(a))
b = bool(a)
print(b, type(b))

# 字典
# 只要字典中有内容,那么在强制类型转换中转换为bool类型变量时 会返回true
# 反之只要字典中为空 那么在强制类型转换后转换得到的是false的值
a = {'name': '京太郎'}
print(a, type(a))
b = bool(a)
print(b, type(b))

a = {}
print(a)
b = bool(a)
print(b, type(b))

# 什么情况下是false
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
