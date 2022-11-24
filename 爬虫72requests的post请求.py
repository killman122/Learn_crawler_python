import random, requests, json

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'spider'
}


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

# url    请求地址
# data   请求参数
# kwargs 字典
response = requests.post(url=url, data=data, headers=headers)
result_json = requests.post(url=url, data=data, headers=headers).json()
obj = json.loads(response.text, encoding='utf-8')
print(response.json(), response.text, obj)
# .json将文件中用{},[]的数据可以取出字典列表中的内容
# print(result_json)

# post请求 是不需要编解码
# post请求的参数是data
# 不需要请求对象的定制
