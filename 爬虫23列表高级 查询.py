# 所谓查找查看指定元素是否存在 包含了in和not in
'''
in 存在 存在结果为true 否则为false
not in 不存在 不存在结果为true 否则为false
'''
food_list = ['锅包肉', '汆白肉', '东北乱炖']
# 判断一下在控制台输入的数据是否在列表中
food = input('请输入您想吃的食物')

# in在列表中判断 某一个元素是否在某一个列表中
if food in food_list:
    print('在')
else:
    print('不在')

ball_list = ['篮球', '台球']
# 在控制台上输入你喜欢的球类判断是否不在这个列表中
ball = input('输入你喜欢的球类')
if ball not in ball_list:
    print('不在')
else:
    print('在')
