import requests
import random
url='https://www.baidu.com/s?'

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
data={
    'wd':'北京'
}

#url   请求资源路径
#params 参数
#kwargs 字典
response=requests.get(url=url,params=data,headers=headers)
print(response.text)
#参数使用params传递
#参数无需urlencode的编码
#不需要请求对象的定制
#请求资源路径中的问号可以加也可以不加