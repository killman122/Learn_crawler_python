import urllib.request, urllib.parse
import random

url = 'https://fanyi.baidu.com/sug'


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
words = input('请输入你要查找的单词:')
# 下面的data数据是请求头中text预览中的内容也是请求头中的负载,而header指的是完整的请求头
headers = {
    'User-Agent': ua
}
data = {
    'kw': words
}
# post请求类型的参数 必须进行编码 将data进行编码转换为字节型数据
data = urllib.parse.urlencode(data).encode()  # 这里的encode中可以不写编码方式,自动选择编码方式

# data=urllib.parse.urlencode(data).encode('utf-8')
print(data, type(data))
request = urllib.request.Request(url=url, data=data, headers=headers)  # 如果要在请求头中加入请求体则要使用data=data在函数的参数内

# post请求的参数 是不会拼接在url后面的但是get请求可以    并且参数是要放在请求对象的定制参数中  也就是上面的request
# print(request)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')
# print(content)

# post 请求方式的参数 必须编码 data=urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data=urllib.request.urlencode(data).encode()

# 字符串变成json对象
import json

obj = json.loads(content)
# 或者写为 result_json = requests.post(url=sign_url, headers=sign_header).json() 可以转换为一个json的对象

# print(obj)
# 尝试转换res为 json 对象，请尝试json.loads(res)而不是res.json(),res是一个字符串，而不是 json 对象，因此没有该.json()属性。
# print(obj['data'],type(obj['data']))
for i in obj['data']:
    # print(i,type(i))
    print(i['k'], i['v'])
# obj1=(obj['data'][0]['v'])
# print(obj1)
# print(obj1,type(obj1),obj1['v'])
# print(obj1['k']['v'])
