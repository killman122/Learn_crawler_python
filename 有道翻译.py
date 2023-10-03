import requests  # 导入请求模块
import pprint  # 导入格式化输出模块
import execjs  # 导入execjs模块可以使用js文件生成的数据
import urllib.parse
import json

while 1:
    i = input("请输入你想查找的单词,如果输入0则退出程序\n")
    if i == '0':
        break
    f = open('有道翻译js代码.js', encoding='utf-8')
    js_code = f.read()
    # print(js_code)
    compile_code = execjs.compile(js_code)  # 对要运行的js代码进行编译
    json_data = compile_code.call('youdao', i)  # 这里是对js代码中的函数进行调用
    # print(json_data)
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"OUTFOX_SEARCH_USER_ID=-1139768419@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=2066572915.1918595; ___rl__test__cookies={json_data['ts']}",
        "Host": "fanyi.youdao.com",
        "Origin": "https://fanyi.youdao.com",
        "Pragma": "no-cache",
        "Referer": "https://fanyi.youdao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
    }
    data = {
        "i": i,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": json_data.get('salt'),  # 使用json_data['salt']会产生语法错误,未申明变量,当键值不存在时,会报错,优先使用get
        "sign": json_data.get('sign'),
        "lts": json_data['ts'],
        "bv": json_data.get('bv'),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    print(f'这是测试输出你想要的data请求头中的数据{data}')

    response = requests.post(url=url, data=data, headers=headers)
    # print(response)
    # print(f'{response.text},数据类型是{type(response.text)}')

    # print(f'{response.json()},数据类型是{type(response.json())}')
    res = response.json()
    print(f"翻译后的结果是:===>{res['translateResult'][0][0]['tgt']}<===")  # 这里不能连续使用两个单引号否则会不闭合
    # print(res['smartResult'],type(res['smartResult']))
    res1=res.get('smartResult')
    if res1:
        # print('数据不为空')
        for i in res['smartResult']['entries']:
            print(f'额外的详细数据是:{i}')
    else:
        print('不存在数据额外详细数据')
# if json_data['smartResult'] is not None:
    #     for i in res['smartResult']['entries']:
    #         print(i)
        # print(f"输出的结果详细是{res['smartResult']}")
    # pprint(response.json())
    # res=response.json()
    # pprint(res)
