import urllib.parse
import random
import urllib.request
import json
#url='https://movie.douban.com/j/chart/top_list?type=16&interval_id=100:90&action=&start=0&limit=20'

#page   1   2   3   4
#start  0   20  40  60

#start (page-1)*20

#下载豆瓣电影的前十页的数据
#(1)请求对象的定制
#(2)获取响应的数据
#(3)下载数据
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

def creat_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=16&interval_id=100:90&action=&'
    data={
        'start':(page-1)*20,
        'limit':20
    }

    data=urllib.parse.urlencode(data)#在get请求中不需要使用encode()

    url=base_url+data
    print(url,type(url))
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
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
        #字符串变成json对象

    obj=json.loads(content)
    print(obj,type(obj))
    for i in obj:
        #print(i,type(i))
        #print(str(i['rank'],i['title']))
        relevant=str(i['rank'])+' '+str(i['title'])
        print(relevant)
        fp=open('豆瓣电影排行.txt','a')
        fp.write(relevant+'\n')
        #print(content,type(content))
        fp.close()
        return relevant
        

def down_load(page,relevant):
    with open('douban_'+str(page)+'.txt','w')as f:
        f.write(relevant)
        #一个函数中只能有返回值一个所以relevant返回后只能在有一个
#主程序程序的入口
if __name__=='__main__':
    start_page=int(input('请输入起始的页码:'))
    end_page=int(input('请输入结束的页码:'))
#   每一页都有自己的请求对象的定制
    for page in range(start_page,end_page+1):
        request=creat_request(page)
        relevant=get_content(request)
        down_load(page,relevant)
        