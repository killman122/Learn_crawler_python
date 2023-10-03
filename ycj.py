import random#此处的模块为随机数模块
import requests#此处模块为请求模块
from tqdm import tqdm#此处模块为进度条模块tqdm()
from loguru import logger#此处模块为日志模块通过输出日期加运行结果的格式输出
import time#时间模块可以用来计算当前时间用作产生时间戳在网址末端
#import response
#import re#导入一个正则表达式模块
import json
#导入模块或者写好的函数
#例如 from img_api import base_64
def get_time():
    now_time=str(int(time.time()*1000))
    print('当前时间戳:',now_time)
    return now_time
#get_time()

ycjaccount = '15933580813'
ycjpassword = '123456'
userid = []
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

# 登录通过def定义一个函数
def login(ua):
    try:
        sign_url = 'http://new.ynyc6666.com/shop/server/user/login?userPhoneNumber='+ycjaccount+'&password='+ycjpassword#此处传递的参数中如果将vcjaccount换为userPhoneNumber+xxx
        #sign_url = 'http://new.ynyc6666.com/shop/server/user/login?userPhoneNumber=15933580813&password=123456'#此处传递的参数中如果将vcjaccount换为userPhoneNumber+xxx
        sign_header = {
'Host':'new.ynyc6666.com',
'Connection': 'keep-alive',
'Content-Length': '0',
'Accept': 'application/json, text/plain, */*',
'User-Agent': ua,
'X-Requested-With': 'XMLHttpRequest',
'Origin': 'http://new.ynyc6666.com',
'Referer': 'http://new.ynyc6666.com/shop/app/?t=1653653726582',#这里的refer用作防盗链
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        #下面的result算是一个接口但是该接口与上面的sign_header算是不同种写入方法的接口填参数
        
        result = requests.post(url=sign_url, headers=sign_header)#如果要在请求头中加入请求体则要使用data=data在函数的参数内
        #print(result)
        html_data=result.text
        #print(html_data)
        #打印出的是一个response对象显示为'<Response 200>',不是直接的响应码如200,302,不能直接用于对象之间判断或者调用
        #如果是请求的一个图片的响应可以使用response.content函数将数据转化为二进制数据
        #所以二进制数据不能直接用做判断
        #使用with open()函数可以将之前的二进制数据保存为某种数据的格式,例如with open('yzm.jpg')
        #with open('yzm.jpg',mode='wb')
                    #f.write(img_data)
        result_json = requests.post(url=sign_url, headers=sign_header).json()
        
        #cookieJar=str(result.cookies)
        #print(cookieJar)
        
        
        #print(result_json)
         #if result_json['status==200']:
        #if result.status_code == 200:
            #userid.append(result_json['data']['sourceUserId'])
            #return '登录成功'
        #else:
            #return '未知错误' + result_json

        if result_json ['code']==0:
            return '登陆失败'
        else:
            userid.append(result_json['data']['sourceUserId'])
            #print(json.loads(html_data))
            #print(html_data.id)
            data=result_json['data']
            #print(data['id'])
            global x
            x=data['id']
            #print(data['points'])
            #print(x)
            #print(result_json['data'])
            print('==============📣系统通知📣==============')
            print('[账号]'+ycjaccount+'登陆成功')
            print('[现有积分]',data['points'])
            return '登陆成功'
        
        
    except Exception as e:
        return e
        

# 签到  在请求的url中可以将后面需要拼接的字符使用+的字符串拼接符表示连接到url之后
#format函数在其中用来格式化字符串

def sign(ua):
    global x#在这里使用global定义了一个全局变量,在这个全局变量的使用过程中就不能以函数传参数的形式将上一个函数中定义的全局变量传入这个函数中
    #print(x)
    try:
        sign_url = 'http://new.ynyc6666.com/shop/server/sign/userSign?userId='+x
        #此处使用.format(userId[0])的意思是从这个userid的输入好的数组中选取第一个数组中的第一行的变量填入,不过此处是没有将三个初始变量写死在脚本中而是通过导入后的方式将原始的数据填入
        sign_header = {
'Connection': 'keep-alive',
'Content-Length': '0',
'Accept': 'application/json, text/plain, */*',
'User-Agent': ua,
'X-Requested-With': 'XMLHttpRequest',
'Origin': 'http://new.ynyc6666.com',
'Referer': 'http://new.ynyc6666.com/shop/app/?t=1653452746153',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        #print(sign_url)#这里用作测试
        result = requests.post(url=sign_url, headers=sign_header) 
        #此处的result等同于响应体
        result_json = result = requests.post(url=sign_url, headers=sign_header).json()#使用xxx.json查看了返回的数据,是在抓包中的json格式数据    json数据似乎是一个字典类
        #print(result_json)
        #print(result_json['data'])#这里用作测试测试是否可以将数据打印
        a=result_json['data']
        
        #cookieJar=result.cookies使用cookiejar的方式获取当前的cookie信息
        #之后使用cookieJar.get_dirt()的方式将cookies打印为一个字典的形式
        if a['msg']=='签到成功':#此处判断所使用的变量在脚本中的状态
            print('[签到成功]')
            return '签到成功'
        else:
            return '签到失败' + result
    except Exception as e:
        return e


if __name__ == '__main__':
    my_ua = get_ua()
    login_result = login(my_ua)
    sign_result = sign(my_ua)
    login_result = login(my_ua)
    #logger.info(login_result)
    logger.info(sign_result)



#eval()将字典内容转换为字符串
json.loads()
# response.split()