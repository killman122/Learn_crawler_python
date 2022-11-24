#需求下载网页的前十页的图片
#https://sc.chinaz.com/tag_tupian/mm131meinv_10.html
#https://sc.chinaz.com/tag_tupian/mm131meinv.html
#(1)请求对象的定制
#(2)获取网页的源码
#(3)下载
import urllib.parse
import random
import urllib.request
import json
from lxml import etree#这里是导入了xpath的模块
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
}
start_page=int(input('请输入起始的下载页码'))
end_page=int(input('请输入终止的下载页码'))
#url='https://sc.chinaz.com/tag_tupian/mm131meinv.html'
for page in range(start_page,end_page+1):
    if page==1:
        page=''
    else:
        page='_'+str(page)
    print(page,type(page))
    url='https://sc.chinaz.com/tag_tupian/mm131meinv'+page+'.html'
    print(url,type(url))
    #请求对象的定制
    request=urllib.request.Request(url=url,headers=headers)
    #获取网页的源码
    response=urllib.request.urlopen(request)
    #获取内容
    content=response.read().decode('utf-8')
    #print(content,type(content))
    #下载内容   下载图片
    #urllib.request.urlretrieve('图片地址','文件的名字')
    #此时需要xpath进行解析
    tree=etree.HTML(content)
    name_list=tree.xpath('//div[@id="container"]//a/img/@alt')
    print(type(name_list))
    img_list=tree.xpath('//div[@id="container"]//a/img/@src')
    #for name in name_list:
    #    i=str(name)
    #    print(i,type(i))
    #    #for img in img_list:
    #    #    l=str(img)
    #for img in img_list:
    #    l=str(img)
    #    print(l)
    #print(name_list[1],img_list[1])
        #print(i,l)
        #url='https'+l
        #print(i,url)
        #urllib.request.urlretrieve(url,i)
    for x in range(len(name_list)):
        print(x)
        name=name_list[x]
        src=img_list[x]
        #print(name,src)
        url='https:'+src
        print(name,url)
        urllib.request.urlretrieve(url=url,filename=name+'.jpg')
    
        #当需要两个变量在不同的循环中循环显示时需要将两个for循环的嵌套,然后将变量在外层循环中显示出
    #for img in img_list:
    #    l=str(img)
    #    print(l,type(l))
        



            
    #for x in name_list,img_list:
    #    print(x,type(x))
    #    for a in x:
    #        i=str(a)
    #        print(i,type(i))
    #        #print(a[0])
        
    #for x in name_list,img_list:
        #print(x,type(x))
        #print(x[0])
        #for a in x:
        #    i=str(a)
        #    print(i,type(i))
        #    #print(a[0])
    