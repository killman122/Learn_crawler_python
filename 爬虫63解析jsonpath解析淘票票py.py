import json 
import urllib.request
import jsonpath
import random
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
#浏览器中的负载选项是请求头中提交的表单
url='https://dianying.taobao.com/showAction.json?_ksTS=1657336435778_64&jsoncallback=jsonp65&action=showAction&n_s=new&event_submit_doGetSoon=true'
headers={
    'User-Agent':ua,
    'Referer':'https://dianying.taobao.com/?spm=a1z21.3046609.city.15.32c0112abwCu8x&city=610900',
    'Cookie':'miid=6715190121633507407; enc=C4wVtAloRVu3ascbTjwWbAg6+aThZicDvSDvsnkZGs41WBA92tDYkW1hbO+NmVu1RbjkVEqaHqyO5Z0bgUBVjBbg8KcJv9FGVfZpR56svsuDejYyCJ0Qxj+qQLnYHKfO; thw=cn; t=7c6cfdfbf266ba41389092bb70812183; cookie2=1c18dcf4e4c854c9b7ddadc3c09cefa9; v=0; _tb_token_=78953edfab767; _m_h5_tk=7ce208e537438da7ebdeed479daab984_1657345968257; _m_h5_tk_enc=8af084254cfa0881095c7c553c10dc14; tb_city=610900; tb_cityName="sLK/tQ=="; isg=BPb2HI_JiIlOunwl-Vux-GO4Ryz4FzpRzetfMmDfwFl0o5Y9yadWYV7av__PEDJp; l=eBIgVX4rLBMMWbHGBOfalurza779dIRYYuPzaNbMiOCPOMfB5qgVW6At7eL6Cn1VhsCHJ3ud9SS9BeYBqWFKnxvTaxom4bHmn; tfstk=ch3FBQceieLF4OnhuPUyOKEfXGhdZ8lnZNPbxK-hXko96cEhiZB8sm97_71NEkf..'
}
#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
#模拟浏览器发出请求
response=urllib.request.urlopen(request)
#获取响应的内容
content=response.read().decode('utf-8')

#print(content.split('('),type(content.split('(')))
#print(content,type(content))
print(content.split('(')[1].split(';')[0].split(')')[0].split('{')[2],type(content.split('(')[1].split(';')))