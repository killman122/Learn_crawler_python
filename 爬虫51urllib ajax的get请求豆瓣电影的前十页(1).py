import urllib.parse
import urllib.request
import requests
import random
import json
start_page=int(input('请输入你要查找的起始页的数据:'))
end_page=int(input('请输入你要查找的结束页的数据:'))

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

headers={
    'User-Agent':ua,
    'Accept': '*/*',
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
for page in range(start_page,end_page+1):
    print(page,type(page))
    page=str((int(page)-1)*20)
    url='https://movie.douban.com/j/chart/top_list?type=16&interval_id=100:90&action=&start='+page+'&limit=20'
    print(url)
    #请求对象的定制
    request=urllib.request.Request(url=url,headers=headers)
    #获取响应的数据
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    #content=resopnse.read().decode()
    #content=response.read()    在不使用decode的方法是会显示未编译的utf-8乱码数据
    
    #print(content,type(content))   #这里是一个字符串内容返回
    #在使用urllib的方法时是返回了一个str类型数据需要转换为json数据,但是直接调用request时是可以使用不需要后续转换为json对象

    #字符串变成json对象

    obj=json.loads(content)
    #print(obj,type(obj))
    for i in obj:
        #print(i,type(i))
        #print(str(i['rank'],i['title']))
        relevant=str(i['rank'])+' '+str(i['title'])
        print(relevant)
        fp=open('豆瓣电影排行.txt','a')
        fp.write(relevant+'\n')


fp.close()
#page=str((int(page)-1)*20)
#print(page,type(page))
#url='https://movie.douban.com/j/chart/top_list?type=16&interval_id=100:90&action=&start='+page+'&limit=20'
#print(url)

