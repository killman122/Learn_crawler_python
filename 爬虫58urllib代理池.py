#简易代理池

import random
import urllib.request
import urllib.parse
proxies_pool=[
    {
        'http':'118.24.219.151:16817'
    },
    {
        'http':'118.24.219.151:16817111'
    },

]

url='http://www.baidu.com/s?wd=ip'
proxies=random.choice(proxies_pool)
print(proxies)
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
headers={
    'User-Agent':ua,
}

#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)

#模拟浏览器来访问服务器
#response=urllib.request.urlopen(request)
handler=urllib.request.ProxyHandler(proxies=proxies)

opener=urllib.request.build_opener(handler)

response=opener.open(request)
#获取响应的信息对信息进行编码处理
content=response.read().decode('utf-8')

#写入
with open('dailichi.html','w',encoding='utf-8')as fp:
    fp.write(content)