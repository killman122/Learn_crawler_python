a = 1
# a加上一个2 打印结果
a = a + 2
print(a)
# 复合赋值运算符
# 与C++中的 +=  -=  *=  /=  %=  <<=  >>=  &=  |=  ^= 的实际作用相同
b = 1
b += 2
print(b)
# 相当于复合赋值运算符留下等于后再将等号左侧的数据用于等号右侧后在返回
# a+=2 <=> a=a+2
# c乘以一个三打印结果
c = 1
c = c * 3
print(c * 3)
# 上面的c的赋值等同与c *= 3


d = 2
# d减去一个1打印结果
d = d - 1
print(d)
# 等同与d-=1

e = 3
# e除以2打印结果
e = e / 2
print(e)
# 等同于e /= 2


f = 3
# f整除一个2后打印结果--即保留小数点前面的字符
f = f // 2
print(f)
f //= 2

# % 取余 取模 模余
f = 3
# f 对5取余数 打印结果
f = f % 5
print(f)
# f %=

# 幂赋值运算符
g = 5
# 求一下5的三次幂
g = g ** 3  # 后面跟的参数是幂数
print(g)
g **= 3
