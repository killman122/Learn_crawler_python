'''
urllib.request.urlopen()模拟浏览器向服务器发送请求 但是在写脚本中一般是使用request模块
response  服务器返回的数据
    response的数据类型是HttpResponse
    字节-->字符串
            解码decode
    字符串-->字节
            编码encode
    read()  字节形式读取二进制  拓展:rede(5)返回前几个字节
    readline() 读取一行数据
    readlines() 一行一行读取 直到结束
    getcode() 获取状态码
    geturl() 获取url
    getheaders() 获取headers
urllib.request.urlretrieve()
    请求网页
    请求图片
    请求视频
'''
import urllib.request
import requests

# 使用urllib来获取百度首页的源码
# 1.定义一个url 就是你要访问的地址
url = 'http://www.baidu.com'
# 2.模拟浏览器向服务器发送请求 response代表响应
response = urllib.request.urlopen(url)
# 3.获取响应中的页面的源码,但是也可以获取到页面的响应码 请求头 响应体等等
# read()方法返回的是字节形式的二进制数据 也就是显示html源码后显示带b开头的就是字节型数据
# 将二进制的数据转换为字符串
# 二进制-->>字符串 解码 decode('编码格式') 的方法进行解码 防止出现字符串的乱码在显示网页源代码的过程中
# 如何查找编码格式 打开html源代码 查看charset 其中显示的就是 编码格式 比如说utf-8 编码之后可以在网页源码中看到汉字
# 所以要对于已经获取的网页源码进行解码
content = response.read().decode('utf-8')
# content=response.read()

result = requests.post(url)
# result_json = requests.post(url).json()
# print(result_json.text)


# print(result.text,type(result.text))
print(result, type(result))
print(type(response))

# 4.打印数据
print(content, type(content))
