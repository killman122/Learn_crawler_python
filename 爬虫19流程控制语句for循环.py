# 循环字符串
# range(5)
# range(1,6)
# range(1,10,3)
# 循环一个列表


# s='china'#这里定义了一个字符串
##一个一个的输出 叫做循环 或者是遍历
# print(s[0],s[1],s[2],s[3],s[4])#以单个数组的形式输出相对应的变量
##for
##格式: for 变量 in 要遍历的数据
##          方法体
##i 是字符串中一个有一个的字符的变量,即无所谓使用i作为变量名或者是使用其余字符用做变量名
# for i in s:
#    print(i)
'''
#range方法的结果是一个可以遍历的对象
for i in range(5):
    print (i)
#range(5)的结果是打印0,1,2,3,4的左闭右开区间类数组的形式开始在不申明起始变量的情况下均已数组的零位开始
#range(1,6)
for i in range(6):
    print(i)
#range 函数中可以写两个参数 第一个参数代表起始值,第二个参数代表结束值 但是实际显示的为结束值的前一个变量
for i in range(1,6):
    print(i)
#range 函数中可以写三个参数 第一个代表参数起始,第二个参数代表参数结束值,第三个参数间隔值也是步长
range(1,10,3)#三个参数的意义(起始值,结束值,步长)步长在未来的切片中包含 这里到九为结束值 应为终止的变量在最后的第二个变量位
for i in range(1,10,3):   
    print(i)

#应用场景  爬取一个列表返回给我,之后对返回值进行遍历
#循环一个列表
a_list=['周杰伦','林俊杰','陶杰']
#遍历列表中的元素
for i in a_list:
    print(i)
#遍历列表中的下标
#len()函数用来判断列表中元素的个数
print(len(a_list))
for i in range(len(a_list)):
    print(i)#显示出该字符串的长度,也就是列表的长的
'''
for i in range(5):
    print(i)
a_list = ['周杰伦', '林俊杰', '陶杰']
print(len(a_list))
for i in range(len(a_list)):
    print(i)  # 显示出该字符串的长度,也就是列表的长的,这里是循环输出在这个a_list的所有序列的索引并且索引都是从一开始

for i in enumerate(a_list):
    print(i)

for i in range(1, 10, 3):
    print(i)
