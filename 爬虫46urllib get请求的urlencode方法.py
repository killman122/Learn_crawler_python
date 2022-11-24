# 应用场景:多个参数在url中时 将多个参数的字符同时转换为unicode码  在这里不使用quote的方法
# 其中英文在unicode编码中不改变
# https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.parse
import urllib.request

data = {
    'wd': '周杰伦',
    'sex': '男'
}
a = urllib.parse.urlencode(data)
##在使用urlencode中使用encode的方法可以将字典中的每一项数据拼接起来并且使用&的方式拼接并且形成字符串数据可以用作添加url末尾的参数
print(a, type(a))
# 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7的网页源码
base_url = 'https://www.baidu.com/s?'  # 这里指的是基础url参数
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
data = urllib.parse.urlencode(data)
print(data, type(data))
url = base_url + data
print(url)
import random


def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    # print(ua)
    return ua


get_ua()
useragent = get_ua()
# print(useragent)
# 请求对象的定制防止反爬机制是解决反爬的第一种手段
headers = {'user-agent': useragent}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
