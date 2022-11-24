'''
列表中常用删除的方法有:
del:根据下标进行删除
pop:删除最后一个元素
remove:根据元素的值进行删除
'''
a_list = [1, 2, 3, 4, 5]
print(a_list)
# 根据下标删除列表中的元素  比如删除元素四 从0开始到4结束
# 爬取的数据中有个别的数据是不想要的 通过下标的方式来删除
del a_list[3]
print(a_list)

# pop 是删除列表中的最后一个元素
b_list = [1, 2, 3, 4, 5]
print(b_list)
b_list.pop()
print(b_list)

# remove 是删除含有指定内容的元素
c_list = [1, 2, 3, 4, 5]
print(c_list)
c_list.remove(5)  # 括号内为元素的值不能加引号
# c_list.remove('5')
print(c_list)

string_list = ['小鸡', '炖', '蘑菇']
print(string_list)
string_list.remove('炖')
print(string_list)
# 使用remove可以删除列表中的任意指定的字段
