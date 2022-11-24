'''
为什么要学习handler处理器
urllib.request.urlopen(url)
不能定制请求头
urllib.request.Request(url,headers,data)
可以定制请求头
Handler
可以用来定制更高级的请求头(随着业务逻辑的复杂 请求对象的定制已经不能满足需求 动态cookie和代理不能使用请求对象的定制)
项目需求    在登陆的时候每次登陆后的cookie都不一样 解决方案使用handler
'''

# 需求 使用handler来访问百度  获取网页源码
# 当然 这里也可以使用urlopen的方法
import urllib.request
import random

url = 'http://www.baidu.com'


def get_ua():
    first_num = random.randint(55, 102)
    third_num = random.randint(0, 5005)
    fourth_num = random.randint(0, 140)
    three_num = random.randint(0, 1245)
    four_num = random.randint(0, 44)
    os_type = [
        '(Windows NT 10.0; Win64; x64)', '(Windows NT6.1; Win64; x64)', '(iPhone; CPU iPhone OS 10_3_1 like Mac OS X)',
        '(X11; Linux x86_64)', '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    edge_version = 'Edg/{}.0.{}.{}'.format(first_num, three_num, four_num)
    chorme_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
    ua = ''.join(
        ['Mozilla/5.0 ', random.choice(os_type), ' AppleWebKit/537.36 ', '(KHTML, like Gecko) ', chorme_version,
         ' Safari/537.36 ', edge_version])
    return ua


ua = get_ua()
headers = {
    'User-Agent': ua,
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 访问网址
# handler    build_opener    open

# 1获取handler对象
handler = urllib.request.HTTPHandler()

# 2通过handler来获取opener对象
opener = urllib.request.build_opener(handler)
# 3调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
