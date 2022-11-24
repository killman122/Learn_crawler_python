import urllib.parse
import urllib.request
import json
import random

# 在爬取网站页面时一般爬取的是Fetch/XHR类型数据
base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
city = input('请输入你想查询的城市:')


# print(city,type(city))


# data=urllib.parse.urlencode(data)
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
headers = {
    'User-Agent': ua,
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Content-Length': '71',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'route-cell=ksa; ASP.NET_SessionId=5x0utbb254ikzwhimh3r5syk; SERVERID=6ee43946432b1a5105f8c6178eb14f6d|1655712281|1655712100',
    'Host': 'www.kfc.com.cn',
    'Origin': 'http://www.kfc.com.cn',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'X-Requested-With': 'XMLHttpRequest',
}
start_page = int(input('请输入起始页码:'))
end_page = int(input('请输入终止页码:'))

for page in range(start_page, end_page + 1):
    print(page)
    data = {
        'cname': city,
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    # print(data)
    data = urllib.parse.urlencode(data).encode('utf-8')
    # print(data,type(data))
    request = urllib.request.Request(url=base_url, data=data, headers=headers)  # 如果要在请求头中加入请求体则要使用data=data在函数的参数内

    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content,type(content))

    obj = json.loads(content)

    # print(obj,type(obj))
    # print(obj['Table1'],type(obj['Table1']))
    for i in obj['Table1']:
        # print(i,type(i))
        # print(i['rownum'],type(i['rownum']))
        print(str(i['rownum']) + ' ' + i['provinceName'] + i['cityName'] + '详细地址' + i['storeName'] + ' ' + i[
            'addressDetail'] + '\n' + '亮点:' + i['pro'])
        relevant = (str(i['rownum']) + ' ' + i['provinceName'] + i['cityName'] + '详细地址' + i['storeName'] + ' ' + i[
            'addressDetail'] + '\n' + '亮点:' + i['pro'])
        fp = open('肯德基相关地址查询.txt', 'a')
        fp.write(relevant + '\n')
        # s=['rownum']+['provinceName']+['cityName']+' '+'详细地址:'+['storeName']+['addressDetail']+'提供'+['pro']
        # print(s)
    # for i in obj:
    #    print(i)
    # print(i['Table'])
