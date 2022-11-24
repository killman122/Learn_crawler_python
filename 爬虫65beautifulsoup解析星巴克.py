import urllib.request

url = 'https://www.starbucks.com.cn/menu/'
# 这里无需请求对象的定制,直接模拟浏览器发出请求
response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')
# print(content)
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')
# xpath写法//ul[@class="grid padded-3 product"]//strong
name_list = soup.select('ul[class="grid padded-3 product"] strong')
print(name_list, type(name_list))
for i in name_list:
    name = str(i)
    print(name.split('<')[1].split('>')[1], type(i))
    print(i.string)  # 在获取bs数据时可以转换为str后再将数据通过split分割出
    # 或者是将bs数据通过string或者get_text()的方式输出
