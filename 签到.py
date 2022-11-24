import requests
import time
import os
import re
import random
import json
import urllib.parse
from tqdm import tqdm #这里是使用窗体的控件
from loguru import logger


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

url = 'http://newcrm.wismall.com/shop/CheckIn/getCheckInData.html'
url1 = 'http://newcrm.wismall.com/shop/CheckIn/checkIn.html'
PHPSESSID = ''

PHPSESSID = ''
if "PHPSESSID" in os.environ and os.environ["PHPSESSID"]:
    PHPSESSID = os.environ["PHPSESSID"]
    PHPSESSID = str(PHPSESSID)
    # print(PHPSESSID,type(PHPSESSID))
    # print(PHPSESSID.split('@'),type(PHPSESSID.split('@')))
    for i in PHPSESSID.split('@'):
        # print(i)
        PHPSESSID = i
        print(PHPSESSID)

headers = {
    'Host': 'newcrm.wismall.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': ua,
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://newcrm.wismall.com/shop/checkIn/index/token/547bcb48040a7.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'PHPSESSID=' + PHPSESSID
}
response = requests.get(url=url, headers=headers)
# print(response,type(response))
result = response.json()
# print(result,type(result))
print(str(result['msg']) + '希币总数:' + str(result['data']['totalIntegral']))
# print(result['data']['totalIntegral'])
time.sleep(3)
response = requests.get(url=url1, headers=headers)
result = response.json()
print(result['status'])
if str(result['status']) == 'False':
    print('签到失败,已经签到过了')
else:
    print(result['msg'])

# print(result)
# print('签到状态'+result.get('msg'))
#.text转换为文本
#.content转换为二进制文件可以用来保存图片
