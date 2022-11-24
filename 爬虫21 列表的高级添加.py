'''
列表高级
列表的增删改查

添加元素
添加元素的方法:
append 在末尾添加元素
insert 在指定位置添加元素
extend 合并两个列表

'''
# append  追加  在列表的最后添加一个对象/数据 追加对象的列表的最后
food_list = ['铁锅炖大鹅', '酸菜五花肉']
print(food_list)

food_list.append('小鸡炖蘑菇')
print(food_list)

# insert 插入 insert()中有两个参数(index,object)
# 其中index的值是你想插入的数据的下标
char_list = ['a', 'c']
print(char_list)
char_list.insert(1, 'b')  # 这里的0号位置是字符a的位置 这里列表变量1的位置是插入元素b的位置
print(char_list)
char_list.insert(2,'f')
print(char_list)
for i in char_list:
    print(i)

# extend  interable要求对象是可以迭代的,也就是要有多个元素
num_list = [1, 2, 3]
num1_list = [4, 5, 6]
num_list.extend(num1_list)
print(num_list)
# 通过extend将列表中的元素逐一添加到另一个列表中

string_list = ['小鸡', '大鹅', '炖']
string_list1 = ['妲己', '小鹅', '煮']
string_list.extend(string_list1)
print(string_list)
# 使用循环迭代的方法 追加列表中的元素

# 列表的遍历中使用for循环在字符串的遍历
num=(1,2,3)
num1=(4,5,6)
list1=list(num).extend(list(num1))
print(list1)
# num.extend(num1) #在元组中不能使用追加追加只能使用在列表中
