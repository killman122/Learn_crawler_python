import requests
import random
url='http://www.baidu.com/s?'
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
ua=get_ua()
headers={
    'User-Agent':ua
}
data={
    'wd':'ip'
}

proxy={
    'http':'121.121.221.112:121'
}

response=requests.get(url=url,params=data,headers=headers,proxoes=proxy)
print(response.text)
with open('代理.html','w',encoding='utf-8')as fp:
    fp.write(response.text)