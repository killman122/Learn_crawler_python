'''
beautifulsoup的使用与lxml的xpath解析相似
可以用来解析与提取数据
'''
from bs4 import BeautifulSoup

# 解析本地文件 来将bs4的基础语法讲解
soup = BeautifulSoup(open('爬虫64.html', encoding='utf-8'), 'lxml')
# 默认打开的文件的编码格式是gbk
# print(soup)输出错误
# 'gbk' codec can't decode byte 0xa1 in position 258: illegal multibyte sequence
# print(soup,type(soup))

# 根据标签名来查找节点
# 找到的是第一个符合条件的数据
# print(soup.a)
# print(soup.a.attrs)#返回了标签的属性和属性值

# bs4的一些函数
# 1.find()
# print(soup.find('a'))#返回第一个 符合数据的a标签
# 根据title的值来找到对应的标签对象
# print(soup.find('a',title="a2"))
# print(soup.find('a',class_="a1"))#class作为关键字不能直接使用但是可以使用_来使用
# 根据class的值来找到对应的标签对象    注意class要添加下划线


# 2.find_all()   返回的是一个列表    并且返回了所有的a标签
# print(soup.find_all('a'))
# 如果想获取的是多个标签的数据,那么需要在find_all的参数中添加的是列表的数据
# print(soup.find_all(['a','span']))#在列表中才能一次性返回多个数据
# limit的作用是查找前几个数据
# print(soup.find_all('li',limit=2))


# 3.select(推荐)
# select方法返回的是一个列表,并且会返回多个数据
print(soup.select('a'))
print(soup.select('.a1'))  # 带有class的页面查找时要加入一个.代表class    我们把这种操作叫做类选择器
print(soup.select('#l1'))
# 属性选择器--通过属性来寻找对应的标签
# 查找到li标签中有id的标签
print(soup.select('li[id]'))

# 查找到li标签中id为l2的标签
print(soup.select('li[id="l2"]'))

# 层级选择器

# 后代选择器
# 找到的是div下面的li
print(soup.select('div li'))
# 子代选择器
# 某标签的第一级子标签
# 注意:很多的计算机编程语言中不加空格不会输出内容   但是在bs4中不会报错会显示内容
print(soup.select('div>ul>li'))
# 找到a标签和li标签的所有的对象
print(soup.select('a,li'))

# 节点信息
# 获取节点内容
obj = soup.select('#d1')[0]  # 返回值为列表不能直接输出需要使用下标或者for循环的方式输出所有 的值
# 如果标签对象中只有内容 那么string和get_text()都可以使用
# 如果标签对象中除了内容还有标签那么string就获取不到数据 而get_text()可以获取到数据
print(obj.string, type(obj))
print(obj.get_text, type(obj.get_text))

# 节点的属性
obj = soup.select('#p1')[0]  # '#'中的内容是需要查找的关键字
# name是标签的名字
print(obj.name)
# 将属性值作为一个字典返回 可以返回多个数据
print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
