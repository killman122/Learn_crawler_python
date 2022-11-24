'''
jsonpath的安装及其使用方式:
    pip安装:
    pip install jsonpath
jsonpath的使用:
    obj=json.load(open('json文件','r',encoding='utf-8'))
    ret=jsonpath.jsonpath(obj,'jsonpath语法')
'''
#使用jsonpath只能解析本地文件
'''
XPath	JSONPath	Description
/	    $	        根元素
.	    @	        当前元素
/	    . or []	    子元素
..	    n/a	        父元素
//	    ..	        递归下降，JSONPath是从E4X借鉴的。
*	    *	        通配符，表示所有的元素
@	    n/a	        属性访问字符
[]	    []	        子元素操作符
        [,]	        连接操作符在XPath 结果合并其它结点集合。JSONP允许name或者数组索引。
n/a	    [start: end: step]	数组分割操作从ES4借鉴。
[]	    ?()	        应用过滤表示式
n/a	    ()	        脚本表达式，使用在脚本引擎下面。
()	    n/a	        Xpath分组
————————————————

'''
import json
import jsonpath

obj=json.load(open('books.json', 'r',encoding='gb2312'))

#print(obj)

#显示出书店的所有书的作者
author_list=jsonpath.jsonpath(obj,'$.store.book[*].author')
#print(author_list,type(author_list))

##显示出所有的作者
#author_list=jsonpath.jsonpath(obj,'$..author')
#print(author_list,type(author_list))

##store的所有元素
#tag_list=jsonpath.jsonpath(obj,'$.store.*')
#print(tag_list)

#store下面的所有price
#price_list=jsonpath.jsonpath(obj,'$..price')
#price_list=jsonpath.jsonpath(obj,'$.store..price')
#print(price_list)

#第三个书
book=jsonpath.jsonpath(obj,'$..book[2]')
print(book)

#最后一本书
last_book=jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
print(last_book)

#前面的两本书
book_list=jsonpath.jsonpath(obj,'$..book[0,1]')

book_list=jsonpath.jsonpath(obj,'$..book[:2]')
print(book_list)

#条件过滤需要在()的前面添加剂一个问号
#过滤出所有包含isbn的书
book_list=jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
print(book_list)

#过滤出哪些书超过了10块钱
book_list=jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)