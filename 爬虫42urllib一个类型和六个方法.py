import urllib.request

url = 'http://www.baidu.com'
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# 按照一个字节一个字节的去读取数据
content = response.read().decode('utf-8')
print(content)

# 返回多少个字节
content = response.read(5)  # 这里括号内的参数5 代表读取 5个字节的数据 在这里输出的是前5个字节的数据 括号内带几个数字代表返回多少字节的数据

# 按行读取数据并且返回了所有行的数据
content = response.readlines()
print(content)
# 但是无论选择是按照行或者字节读取,在没有使用decode('')的方法下都是二进制存在乱码

# 返回状态码 判断代码是否写的有问题
print(response.getcode())

# 返回url地址
print(response.geturl())

# 返回状态信息以及响应头
print(response.getheaders())
