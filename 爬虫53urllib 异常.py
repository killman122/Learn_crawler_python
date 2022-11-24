import urllib.parse
import urllib.request
import json
import requests
import random
import urllib.error
'''
HTTPError类是URLError类的子类
导入包urllib.error.HTTPError   urllib.error.URLError
http错误:http错误针对浏览器无法连接到服务器而增加的错误提示,引导告诉浏览者是哪里出现了问题
通过urllib发送请求的时候,可能会发送失败 通过try...Exceptiion捕捉异常,异常有两类,URLError\HTTPError
'''
url='https://blog.csdn.net/chixujohnny/article/details/533019951'
def get_ua():
    first_num=random.randint(55,102)
    third_num=random.randint(0,5005)
    fourth_num=random.randint(0,140)
    three_num=random.randint(0,1245)
    four_num=random.randint(0,44)
    os_type=[
        '(Windows NT 10.0; Win64; x64)','(Windows NT6.1; Win64; x64)','(iPhone; CPU iPhone OS 10_3_1 like Mac OS X)','(X11; Linux x86_64)','(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    edge_version='Edg/{}.0.{}.{}'.format(first_num,three_num,four_num)
    chorme_version='Chrome/{}.0.{}.{}'.format(first_num,third_num,fourth_num)
    ua=''.join(['Mozilla/5.0 ',random.choice(os_type),' AppleWebKit/537.36 ', '(KHTML, like Gecko) ',chorme_version,' Safari/537.36 ',edge_version])
    return ua
ua=get_ua()

#print(ua,type(ua))
headers={
    'User-Agent':ua,
}
#print(headers,type(headers))
#请求对象的定制
try:
    request=urllib.request.Request(url=url,headers=headers)
    #模拟浏览器向服务器发送请求
    response=urllib.request.urlopen(request)
    content=response.read().decode('UTF-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.URLError:
    print('我都说了系统正在升级...')