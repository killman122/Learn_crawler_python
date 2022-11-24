'''
三种解析方式比如说获取网页中某一部分的图片源码不是整个网页数据
xpath解析 beautifulsoup解析   jsonpath解析

'''
# xpath解析
# 帮助编程者获取网页源码中的部分数据
from lxml import etree  # 这里的from指的是库与logger的库相同类型 使用from导入ku再通过import导入model

# xpath解析    这里使用lxml解析
# (1)本地文件
# (2)服务器响应文件 response.read().decode('utf-8')
# 解析本地文件使用的是etree.parse('xx.html')
# 解析服务器响应文件使用etree.HTML(response.read().decode('utf-8'))
tree = etree.parse('爬虫59xpath框架的使用.html')  # xpath解析本地文件
# print(tree)
# tree.xpath('xpath路径')
# 使用xpath解析后的文件为列表的格式
'''
1.查询语法
//:查找所有子孙节点,不考虑层级关系 无限嵌套所有的子节点
/:查找直接子节点
2.谓词查询
'''
# 查找ul下面的li
li_list = tree.xpath('//body/ul/li')
print(li_list)
# 判断列表的长度
print(len(li_list))
# 查找所有id的属性的li标签
# text()获取标签中的内容
li_list = tree.xpath('//ul/li[@id]/text()')
# 在浏览器的xpath中查找的过程中要显示其中的内容不需要添加方括号

# 查找id为l1的标签
li_list = tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list)
# 查找到id为l1的li标签的class属性值
li = tree.xpath('//ul/li[@id="l1"]/@class')
print(li)

# 模糊查询
# 查询id中包含l的li标签
li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list)

# 查询id的值以l开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 查询id为l1和class为c1的
li_list = tree.xpath('//ul/li[@id="l1" and class="c1"]/text()')

# 逻辑运算或运算
li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
