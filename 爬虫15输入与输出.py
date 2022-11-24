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
print('我的名字是%s,我的年龄是%d' % (name, age))  # 传入两个参数到%后的数据中

# 输入 input()
passwd = input('请输入您的银行卡密码')
print('我的密码是' + passwd)
print('我的密码是' + str(passwd))
print('我的密码是%s' % passwd)
