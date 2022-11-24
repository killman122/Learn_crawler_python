# 数据类型高级
# 字符串高级
'''
字符串的常见操作:
    获取长度 len() len函数可以获取字符串的长度
    查找内容 find() find函数可以查找指定内容在字符串中是否存在,如果存在就返回该内容在字符串中第一次出现的开始位置索引值,如果不存在,则返回1
    判断:startswitch,endswitch  判断字符串是不是以某某某开头或者结尾  如果是返回true 否则返回false
    计算出现次数 count  返回str在start和end之间 在mystr中出现的次数
    替换字符 replace  替换字符串中的指定的内容,如果指定次数count,则替换不会超过count次
    切割字符串 split  通过参数的内容切割字符串
    修改大小写 upper,lower 将字符串中的大小写互换
    空格处理 strip q  去除空格
    字符串拼接  join 字符串拼接
'''
# len 是length的缩写 用来判断字符串或者列表的长度
s = 'china'
print(len(s))

s1 = 'china'
print(s1.find('c'))  # 返回的数据是寻找的字符在字符串中的位置

s2 = 'china'
print(s2.startswith('c'))  # 返回真或假如果是以c开头以a结尾则返回真,反之未找到返回假
print(s2.endswith('a'))

s3 = 'aaabb'
print(s3.count('a'))
print(s3.count('b'))

s4 = 'cccdd'
print(s4.replace('c', 'd'))  # 将字符串中的指定功能替换  将两个参数中的第一个变量与中间的第二个变量互换

# 指定字符串切割某一部分就是将字符串中的数据剥离出
# split()的分割函数  这通用与分割字符串 可以用作在脚本的写作过程中分割出不同的变量用作多账号的输入
s5 = '1#2#3#4#5#'
print(s5.split('#'))

s5 = 'sasas&12345'
print(s5.split('&'))
ss5 = s5.split('&')
print(ss5)

s6 = 'china'
print(s6.upper())  # 小写字符转换为大写字符
s7 = 'CHIN'
print(s7.lower())  # 大写字符转换为小写字符

s8 = '   a   b'
print(len(s8))  # 在去除空格的过程中 只能去除最前面或者最后面的空格 但是不能去除在两个字符串中间的空格
print(len(s8.strip()))  # 去除空额计算长度结果为5

# 将join前的字符加入join后的字符,从第一个元素开始加,最后一个元素不加
# 用于将序列中的元素以指定的字符连接生成一个新的字符串
s9 = 'hello'
print(s9.join('a'))
s9 = 'a'
print(s9.join('hellow'))  # 连接任意数量的字符串调用其方法的字符串插入到每个给定字符串之间。结果作为新字符串返回。
print('.'.join(['ab', 'pq', 'rs']))
# print('.'.join([111, 222, 333]))  # 这里为整型错误

symbol = "-";
seq = ("a", "b", "c");  # 字符串序列
print(symbol.join(seq)); # print('-'.join('a','b','c'))   print('-'.join(seq))
# a-b-c
