# 1获取网页的源码
# 2 解析 解析的服务器响应的文件 etree.HTML
# 3 打印

import urllib.request
import random
from lxml import etree

url = 'https://www.baidu.com'


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

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取响应内容并编码
content = response.read().decode('utf-8')
# print(content)

# 解析网页源码获取想要的数据
# 解析服务器响应文件 解码服务器的html文件从中寻找有用的数据值
tree = etree.HTML(content)

# 获取想要的数据
result = tree.xpath('//input[@id="su"]/@value')
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)
# xpath的返回值是一个列表类型数据
