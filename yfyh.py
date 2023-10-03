import random #:1此处导入的模块实现的是随机数的功能
import requests #:2这里是一个请求模块,可以使用urllib.requests的模块组代替
from loguru import logger #:3这里需要使用第三方的pip安装模块不是python自带的
import time#这里是导入了一个时间的模块 时间模块一般用作生成时间戳用于请求
def get_time():
    now_time=time.time()#在这里使用time.time()类的方法实现显示当前时间的功能
    print('当前时间戳:',now_time)
    return now_time #这里返回了当前时间 可以用作当在调用时间类的时候返回时间戳
get_time()
'''
频道链接:https://t.me/maomaoalal  交流群:https://t.me/+5xDWXXg-Ug03ZGI1
鸾凤玉华 小程序
抓包 api.luanfengyuhua.cn 域名
变量：sessionkey  
签到10天大概20缘值 价值20块钱
也可以兑换实物
corn 一天一次
'''

# 账号配置

sessionkey_list =['PsXvW6VOEBWk3f4F3MK0aw==']# 多账号配置 ['session1','session2']#这里寻找的登陆时所需要的是什么存储登陆数据的方式 是通过session的方式还是通过cookie的方式,或者是通过帐号以及密码登陆 此处的重点在于分析抓到的数据包 了解 数据包的组成
info ='''
频道链接:https://t.me/maomaoalal  交流群:https://t.me/+5xDWXXg-Ug03ZGI1#这里使用了info相当于提供了一个作者的信息也就是打印输出 但是并不是使用print的方式输出
鸾凤玉华 小程序账号配置
抓包 api.luanfengyuhua.cn 域名
变量：sessionkey  
签到10天大概20缘值 价值20块钱
也可以兑换实物
corn 一天一次
'''#:25
def get_ua ():#:26
    firstnum =random .randint (55 ,62 )#:27
    third_num =random .randint (0 ,3200 )#:28
    fourth_num =random .randint (0 ,140 )#:29
    os_type =['(Windows NT 6.1; WOW64)','(Windows NT 10.0; WOW64)','(X11; Linux x86_64)','(Macintosh; Intel Mac OS X 10_12_6)']#:33
    chrome_version ='Chrome/{}.0.{}.{}'.format (firstnum ,third_num ,fourth_num )#:34
    ua =' '.join (['Mozilla/5.0',random .choice (os_type ),'AppleWebKit/537.36','(KHTML, like Gecko)',chrome_version ,'Safari/537.36'])#:38
    return ua #:39
def Sign (ua ,SessionKey ):#:42这里使用try...except的方法进行错误日志和异常的输出 但是不使用这样的方法并不影响正常使用但是缺失了异常处理的功能
    try :#:43
        sign_url ='https://api.luanfengyuhua.cn/Api/Signin/submit'#:44
        sign_header ={'crypt':'563ed8d6cc76e33bc5cd03ea95bc200c-1653397581000','sessionkey':SessionKey ,'User-Agent':ua ,'content-type':'application/json','Accept-Encoding':'gzip,compress,br,deflate','Referer':'https://servicewechat.com/wx0a33ac3ad3f4c06c/44/page-frame.html',}#:52
        result_json =requests .post (url =sign_url ,headers =sign_header ).json ()#:53
        if result_json ['status']==200 :#:54
            return '签到成功'#:55
        elif result_json ['status']==100 :#:56
            return '今日已签到'#:57
        else :#:58
            return '未知错误'+result_json #:59
    except Exception as e :#:60
        return e #:61
if __name__ =='__main__':#:64
    #logger .info (info )#:65
    logger .info (f'当前共{len(sessionkey_list)}个账号')#:66
    my_ua =get_ua ()#:67
    for sessionkey in sessionkey_list :#:68
        Sign_result =Sign (my_ua ,sessionkey )#:69
        #logger .info (Sign_result )#:70
        print(Sign_result)