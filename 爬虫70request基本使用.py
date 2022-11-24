'''
r=request.get('网址',auth=('',''))
r=request.get(url=url,headers=headers,data=data)
request的属性以及类型
r.text  :获取网站源码 以字符串的形式
r.encoding  :访问或定制编码方式
r.url       :获取网页的url
r.content   :响应的字节类型
r.status_code:响应的状态码
r.headers   :响应的头信息
'''
import requests
import random
url='https://www.baidu.com'
url1='https://www.jd.com'
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
    'User-Agent':ua
}
print(headers)
response=requests.get(url=url,headers=headers)
print(response.text,type(response))#以字符串的形式返回网页的源码
#一个类型和六个属性
#Response类型


#设置响应的编码格式
#response.encoding='utf-8'
#返回的是二进制的数据
#print(resonpse.content)