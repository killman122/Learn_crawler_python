from selenium import webdriver
import time
from selenium.webdriver.common.by import *
from selenium.webdriver.common.by import By
path='msedgedriver.exe'
broswer=webdriver.Edge(path)

url='https://www.baidu.com'
broswer.get(url)

input=broswer.find_element(By.ID,'su')

print(input.get_attribute('class'))#获取属性值
print(input.tag_name)#获取标签名

#获取元素文本
a=broswer.find_element(By.LINK_TEXT,'新闻')
print(input.text)#获取两个标签之间的数据<a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>