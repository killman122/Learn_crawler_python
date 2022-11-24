# 在使用vs注释多行语句时 先点击ctrl+K 之后点击ctrl+c
# 取消多行注释 先点击ctrl+K 之后点击ctrl+U
import urllib.request

url = 'http://www.baidu.com'
url1 = 'https://www.baidu.com'

# url的组成
# 协议 两种http\https   主机 就是网站的域名或者是ip地址       端口号 http:80 https:443    mysql:3306  oracle:1521  redis 6379     mongodb:27017   路径(是s或者是参数前的也就是问号前的)  参数(问号后面填入的)  锚点
# https 更加安全 其中加入了ssl的证书验证
response = urllib.request.urlopen(url1)#直接输出response输出的是<http.client.HTTPResponse object at 0x000001AEC3D8E3C8>
content = response.read().decode('utf-8')
print(content)
# 在打印后发现输出的特别少,因为网站的反爬机制  所以需要伪装请求(加入代理agent 和一些其他请求头中的参数)
# 但是在实际的脚本编写过程中 将ua一般不使用字典的类型保存数据,而是使用字符串类型保存数据,最后将所有的请求头中的参数保存到字典中
# 即使在实际编写中也不能直接将字典中的值直接写在参数中,而是采用赋值的方法,将字典的值赋值给一个参数中的对象
# 因为urlopen的方法中不能存入字典 所以字典ua不能直接传递到参数中
# 实际在使用requeset模块时也是不能将headers的请求头字典直接放在参数中
ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
}
# 在实际的是使用中通过request传递的参数中似乎只有(url ,headers)
# request=urllib.request.Request(url1,ua)

# 或者是使用urllib.request.urlopen的前提是先使用另一个变量用作传递参数
# 因为参数顺序的问题 不能直接写url和headers 中间还有data 所以需要关键字传参
# 指定关键字变量
request = urllib.request.Request(url=url1, headers=ua)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
