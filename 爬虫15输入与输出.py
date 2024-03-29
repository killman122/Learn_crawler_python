# 普通输出print
print('故事里的小黄花,从出生那年就飘着')

# 格式化输出(复杂输出)
# scrapy框架的时候  放入excel 或者mysql redis 中
age = 19
name = '王道'
print('我的年龄是', age)
# 错误写法print('我的年龄是'+18)但是字符串与整型数据不可在一起,通过字符串拼接符
print('我的年龄是' + str(age))

# %s 代表字符串  %d代表数值(无论整数还是浮点数)
print('我的名字是%s,我的年龄是%d' % (name, age))  # 传入两个参数到%后的数据中 在输入多个参数到字符串中的时候:对于字符串/字符使用%s写在要填写的字符串中,对于数据类型(比如整型,小数浮点型等)使用%d代替;对于传入

# print('我的名字叫做%S'%name) 通过使用S和D的切换换为s和d发现和原来的简单字符串的输出不同
print('我的名字叫做%s'%name)
print('我的年龄是%d'%age)
# print('我的年龄是%D'%age) 在单独输出字符串或者是数字类型数据时可以将字符串和要填写的变量分别写在前后的,但是对于多个参数的填入或者输出的时候可以使用元组类型的数据,但是按理说使用可计量的数据类型中是可以使用列表类型数据

# 测试能否将列表类型的数据传入,如果将列表类型上的数据可以传入,表示可以计量的数据类型都是可以当作传入的,但是我觉的只有元组类型可以
# 需要注意的是在使用元组类型传入参数时,将%只是写在所有元组的外边,在元组内的元素处理中将不在填写%
# print("列表类型传入数据测试++++++++++传入字符串%s,传入数据%d"% [name,age])   实测发现如果不使用元组类型的数据传入,则会爆出异常


# 输入 input()
passwd = input('请输入您的银行卡密码')
print('我的密码是' + passwd)
print('我的密码是' + str(passwd))
print('我的密码是%s' % passwd)
