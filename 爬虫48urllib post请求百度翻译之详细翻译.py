'''
这里使用百度翻译的详解接口v2raytranslate
'''
import urllib.request
import urllib.parse
import random

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
url1 = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'


# 随机UA函数
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
print(ua)
print(random.choice(['剪刀', '石头', '布']))
# 这里的随机选取字符串是在列表中,可以是列表中的字符串也可以是列表中的纯数字

# Fromdata 参数中的数据 指的就是浏览器抓包显示的请求标头
headers = {
    # 'User-Agent': ua,
    # 'Accept': '*/*',
    ##'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '136',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=C87B79260DF56AFC4FA941C9DA756437; PSTM=1632371381; BAIDUID=C87B79260DF56AFC6A41A24C9FF12A53:FG=1; __yjs_duid=1_d726232cc5b5ef8d6f36da95f55fc7e71632373109980; BDUSS=VZhLWt2R3I5a1ZCNHFYeXhLVlA0S25XLVBrS1N4dFRkOXUwYXJ2d1ByM0tMS1JoRVFBQUFBJCQAAAAAAQAAAAEAAAA8ZWMtzfXI~cu80-vS8rn7wtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMqffGHKn3xhQ; BDUSS_BFESS=VZhLWt2R3I5a1ZCNHFYeXhLVlA0S25XLVBrS1N4dFRkOXUwYXJ2d1ByM0tMS1JoRVFBQUFBJCQAAAAAAQAAAAEAAAA8ZWMtzfXI~cu80-vS8rn7wtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMqffGHKn3xhQ; H_WISE_SIDS=110085_127969_184716_185638_189660_191248_194085_194519_194530_196428_197241_197711_197956_199023_199176_199579_201193_203310_203517_203525_203880_203883_203886_204122_204713_204715_204717_204720_204919_205218_205420_205424_206007_206196_206930_207234_207264_207716_207830_207884_208267_208721_208816_209395_209512_209568_209749_209841_209944_210069_210097_210300_210359_210404_210521_210670_210709_210733_210737_210890_210893_210895_210906_210969_211059_211062_211180_211207_211302_211305_211335_211350_211441_211457_211531_211580_211736_211755_211785_211860_212226_212293_212416_212617_212627_212699_212772_212797_212830_212869_212962_212967; BAIDUID_BFESS=C87B79260DF56AFC6A41A24C9FF12A53:FG=1; ZFY=gOxLnWdmAsvebKsQZ963FmgfutkGWgj75yfRbZ6up9A:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655377125',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Pragma': 'no-cache',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': '016c8259007f4b80a059d0bcb6b9a3cc',
    'domain': 'common',
}
print(data)
# post请求的参数 必须进行编码 并且调用encode方法
data = urllib.parse.urlencode(data).encode()
print(data,type(data))
request = urllib.request.Request(url=url1, data=data, headers=headers)  # 如果要在请求头中加入请求体则要使用data=data在函数的参数内

# post请求的参数 是不会拼接在url后面的但是get请求可以    并且参数是要放在请求对象的定制参数中  也就是上面的request
# print(request)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
# content=response.read().decode('utf-8')
content = response.read().decode()
# print(content)

# post 请求方式的参数 必须编码 data=urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data=urllib.request.urlencode(data).encode()

# 字符串变成json对象
import json

obj = json.loads(content)
# 或者写为 result_json = requests.post(url=sign_url, headers=sign_header).json() 可以转换为一个json的对象
'''
在使用json的过程中,可以将数据转换为原本的可见数据类型而不是byte类型的数据
'''

print(obj)
# 尝试转换res为 json 对象，请尝试json.loads(res)而不是res.json(),res是一个字符串，而不是 json 对象，因此没有该.json()属性。
# print(obj['data'],type(obj['data']))
# for i in obj['data']:
#    print(i,type(i))
#    print(i['k'],i['v'])
# obj1=(obj['data'][0]['v'])
# print(obj1)
# print(obj1,type(obj1),obj1['v'])
# print(obj1['k']['v'])
