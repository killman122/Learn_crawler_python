# 返回值:函数在完成一个事之后,最后返回给调用者的结果
# 返回值的关键字是return 存在函数中

def buyIceCream():
    return '冰激凌'


# 使用一个变量来接收函数的返回值
food = buyIceCream()

print(food)
print(buyIceCream())


# 案例练习
# 定义一个函数 然后让函数计算两个数值的和 并且返回这个计算之后的结果

def sum():
    a = input('请输入第一个数')
    b = input('请输入第二个数')
    return int(a) + int(b)


print(sum())


# 老师的写法
def sum(a, b):
    c = a + b
    return c


print(sum(123, 456))
