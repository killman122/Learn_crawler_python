import urllib.parse
import urllib.request
import requests
import random
page=input('请输入你要查找的第多少页的数据:')

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
page=str((int(page)-1)*20)
print(page,type(page))
url='https://movie.douban.com/j/chart/top_list?type=16&interval_id=100:90&action=&start='+page+'&limit=20'
headers={
    'User-Agent':ua,
    'Accept': '*/*',
    #'Accept-Encoding': 'gzip, deflate, br',
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
    'X-Requested-With': 'XMLHttpRequest'
}
#请求对象的定制    这里使用request模块
request1=requests.get(url=url,headers=headers)
#获取响应的数据
response=requests.get(url=url,headers=headers).json()
#print(request1)
#print(response,type(response))
open('豆瓣电影排行.txt','w')
for i in response:
    #print(i['rank'],i['title'])
    fp=open('豆瓣电影排行.txt','a')
    relevant=str(i['rank'])+' '+str(i['title'])
    print(relevant)
    fp.write(relevant+'\n')
    #fp.write(str(i['rank'])+'\n'+str(i['title']))

fp.close()
