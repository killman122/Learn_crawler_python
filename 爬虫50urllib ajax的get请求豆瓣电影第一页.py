import urllib.parse
import urllib.request
import random
import json


# 这里是根据收集的ua所编写的随机的ua集合
def get_ua():
    first_num = random.randint(55, 102)
    third_num = random.randint(0, 5005)
    fourth_num = random.randint(0, 140)
    three_num = random.randint(0, 1245)
    four_num = random.randint(0, 44)
    os_type = [
        '(Windows NT 10.0; Win64; x64)', '(Windows NT6.1; Win64; x64)', '(iPhone; CPU iPhone OS 10_3_1 like Mac OS X)',
        '(X11; Linux x86_64)', '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    edge_version = 'Edg/{}.0.{}.{}'.format(first_num, three_num, four_num)
    chorme_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
    ua = ''.join(
        ['Mozilla/5.0 ', random.choice(os_type), ' AppleWebKit/537.36 ', '(KHTML, like Gecko) ', chorme_version,
         ' Safari/537.36 ', edge_version])
    return ua


ua = get_ua()
print(ua)
page = str(input('请输入你要查找的前多少排行:'))
print(page, type(page))
url = 'https://movie.douban.com/j/chart/top_list?type=16&interval_id=100:90&action=&start=0&limit=' + page
print(url, type(url))
headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'bid=yRMDm-8Bhfs; douban-fav-remind=1; ll="108288"; ap_v=0,6.0',
    'Host': 'movie.douban.com',
    'Pragma': 'no-cache',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%A5%87%E5%B9%BB&type=16&interval_id=100:90&action=',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': ua
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content,type(content))   这里是一个字符串内容返回
# 在使用urllib的方法时是返回了一个str类型数据需要转换为json数据,但是直接调用request时是可以使用不需要后续转换为json对象

# 字符串变成json对象

obj = json.loads(content)
# 或者写为 result_json = requests.post(url=sign_url, headers=sign_header).json() 可以转换为一个json的对象

# print(obj,type(obj))
# print(list(content))
# 打开文件并且对文件进行写入
# f=open('text.txt','w')
# print('title')
for i in obj:
    # print(i)
    f = open('text.txt', 'a')
    # print(i['title'],type(i['title']))
    # f.write(i['title'])
    f.write(i['title'] + '\n')
    # f.write()

f.close()
'''
在不使用obj对象的情况下,并且使用utf-8编码所以需要解码
open方法默认情况下使用的是gbk的编码   如果需要在open方法中指定编码格式为utf-8
encoding='utf-8'
fp=open('douban.json','w',encoding='utf-8')
fp.write(content)

with open('douban1.json','w',encoding='utf-8')
fp.write(content)
'''
