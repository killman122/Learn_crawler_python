# 元组与列表类似,不同之处在于元组的元素不能修改,元组使用小括号列表使用方括号 字典使用{}大括号
# 列表中元素直接使用方括号进行修改

a_tuple = (1, 2, 3, 4)
print(a_tuple[0])
print(a_tuple[1])
# a_tuple[0] = 1元组中的内容不能直接通过方括号序列修改
# print(a_tuple)

'''
#元组不可修改里面的内容
#a_tuple[3]=5
#print(a_tuple)
a_list=[1,2,3,4]
a_list[0]=4
print(a_list)
#列表中的元素是可以修改的,列表可以修稿里面的内容
#当定义只有一个元素的元组,需要在唯一的元素后面加一个逗号
a_tuple=(5)
print(type(a_type)
#当一个元组中只要一个元素的时候  那么他是整型数据
'''
b_tuple = (5,)
print(b_tuple, type(b_tuple))
b_tuple = (5)
print(b_tuple, type(b_tuple))

dict = {'姓名': '王道', '年龄': 18}
print(dict, type(dict))
print(dict['姓名'])  # 在数据转换为字典格式后可以通过指定变量名输出变量对应的值
# 另外列表和元组是直接输入全部的变量所以在使用参数作为网链的参时只能使用字典或者json格式的数据
