# 在控制台上输入您的成绩分数
# 如果你考了90分以上 成绩为优秀
# 如果你考了80分以上 成绩为良好
# 如果你考了70分以上 成绩为中等
# 如果你考了60分以上 成绩为及格
# 否则成绩为不合格

# 等同与C++的switch 和case语句
"""
# 错误案例
score = int(input('亲输入您的分数'))
if score >= 90:
    print('优秀')
if score >= 80:
    print('良好')
if score >= 70:
    print('中等')
if score >= 60:
    print('及格')
else:
    print('不及格')
"""
# 使用错误案例输出会全部判断不是判断到合适条件后退出
# 如果是在C++中可以使用break在switch语句的后面,知道最后一个也就是前面的条件排除后可以使用default语句用来代表所有的不符合上述条件的一个集合,反之可以使用return语句在每一个ifelse语句之后


# 正确的使用方法在python中使用elif语句
score = int(input('请输入您的分数:'))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('及格')
else:
    print('不及格')

# 如果直接写成else if那么会报错,所以必须使用else if 的缩写 在多条件分支语句中只能使用elif
# else 语句只能使用 所有的数据判断完整后的锁死判断
'''
score=int(int('请输入您的分数:'))
if score >=90:
    print('优秀')
else:
    print('中等')
但是在使用else 之后后面的所有信息只能有一个约束条件
    
'''
