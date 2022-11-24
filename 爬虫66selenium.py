import urllib.request
import time
url='https://www.jd.com'
from time import sleep

response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
#print(content)

#(1)如何安装selenium
from selenium import webdriver#导入selenium

#(2)创建浏览器操作对象
#global path
path='msedgedriver.exe'
global browser
#browser=webdriver.ChromiumEdge(path)
browser=webdriver.Edge(path)

#(3)访问网站
#url='https://www.baidu.com'
browser.get(url)
time.sleep(100)
content=browser.page_source



print(content)