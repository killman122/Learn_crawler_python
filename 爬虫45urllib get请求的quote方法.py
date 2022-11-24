# 锚点 在参数填写完成后 的可以去除的无关变量
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 需求 获取 https://www.baidu.com/s?wd=周杰伦 的网页源码
import urllib.request
import urllib.parse
import random

url = 'https://www.baidu.com/s?wd=周杰伦'
url2 = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'


def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = (
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    )  # 将列表替换成元组也可以都可以[]=>()
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    print(ua)
    return ua


useragent = get_ua()
print(useragent)
# 请求对象的定制防止反爬机制是解决反爬的第一种手段
# headers={'user-agent': useragent}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'}
# 模拟浏览器发出请求

# request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
# 获取响应的内容
# content=response.read().decode('utf8')
# print(content,type(content))

# get请求方式     将汉字等转换为unioncode码
# urllib.parse.quote()
# 将文字变为unicode编码的格式
# 我们需要依赖与urllib.parse
name = urllib.parse.quote_plus('Lisa')
name1 = urllib.parse.quote_plus('周杰伦')
url1 = 'https://www.baidu.com/s?wd=' + name1

print(name, type(name), name1, url1, type(url1))
request = urllib.request.Request(url=url1, headers=headers)
response = urllib.request.urlopen(request)
print(response, type(response))
content = response.read().decode('utf-8')
# print(content,type(content))
