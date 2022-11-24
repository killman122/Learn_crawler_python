# 通过登陆进入到主界面

# 通过找登录接口


# __VIEWSTATE: ZPv1oG+8AlQGJE1QXPt8UKNRo1+k+1qzvDDeXjNth215iyd0hsFJ/xjp9zZB/pwOYbDV5djTZBMYfTXWwsIIKMFzcJrmHXZ7ZomzzYxay7WRZ+XGCr7mxwl5CZFa9n7slWD/EWjadJs7d0P6I94hl3sC3os=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 2483484885@qq.com
# pwd: 111111
# code: 78MQ#验证码
# denglu: 登录

# 前两个为变量 一般情况下看不到的数据存在于网站的源码中    观察到数据在页面的源码中需要获取页面的源码 然后进行解析获取
# 验证码为变量

import requests
import random
from bs4 import BeautifulSoup
from lxml import etree


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
    return ua


ua = get_ua()
headers = {
    'User-Agent': ua
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

# 获取页面的源码
response = requests.get(url=url, headers=headers)
content = response.text
print(content)

# //div[@class]//input[@type="hidden" and @name="__VIEWSTATE"]/@value
# //div//input[@type="hidden" and @name="__VIEWSTATEGENERATOR"]/@value

# 解析页面源码获取   __VIEWSTATE:    __VIEWSTATEGENERATOR
soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')  # 根据已知属性的值
# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('values')
print(viewstate, viewstategenerator)

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
print(code_url)

# 有坑
import urllib.request

urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# 获取验证码的图片到本地    观察验证码之后 然后在控制台输入这个验证码
# code的参数  就可以下载到本地
code_name = input('请输入你的验证码')

# 点击登陆
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': 'viewstate',
    '__VIEWSTATEGENERATOR': 'viewstategenerator',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2483484885@qq.com',
    'pwd': 'wjr123456',
    'code': 'code_name',
    'denglu': '登录',
}

response_post = session.post(url=url, headers=headers, data=data_post)  # 此处不能用request只能使用session
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)

# reuqest里面有一个方法session()    通过session的返回值   就能使请求变成同一个对象
session = requests.session()
# 验证码的url的内容
response_code = session.get(code_url)
# 注意此时要使用二进制数据   因为要下载的是图片
content_code = response_code.content
# wb 模式将二进制数据写入文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

# 保证验证码请求与网页登陆请求是同一个
