'''
selenium 元素定位:自动化通过模拟鼠标以及键盘操作这些元素,进行点击以及输入,操作这些元素,通过WebDriver提供的元素定位法
方法:
    1.find_element_by_id
       eg:button=browser.find_element_by_id('su')
    2.find_elements_by_name
       eg:name=broswer.find_element_by_name('wd')
    3.find_elements_by_xpath
       eg:xpath1=browser.find_elements_by_xpath('//input[@id="su"]')
    4.find_elements_by_tag_name
       eg:names=broswer.find_elements_by_tag_name('input')
    5.find_element_by_css_selector
       eg:my_input=broswer.find_elements_by_css_selector('akw')[0]
    6.find_elements_by_link_text
        eg:browser.find_element_by_link_text("行文")
'''
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import *
import time
path=''
broswer=webdriver.Edge(path)#创建浏览器对象

url='https://www.baidu.com'
broswer.get(url)




#元素定位
#根据id来找到对象
#button=broswer.find_element(By.ID,'su')
#print(button)
#time.sleep(100)

#根据标签属性的属性值
#button=broswer.find_element(By.NAME,'wd')#z这里的name指的是属性的值
#print(button)

#根据xpath语句获取对象
#button=broswer.find_element(By.XPATH,'//input[@id="su"]')
#print(button)

#根据标签的名字来获取对象
#button=broswer.find_elements(By.TAG_NAME,'input')
#print(button)

#使用bs4的语法来获取对象
#button=broswer.find_elements(By.CSS_SELECTOR,'#su')
#print(button)

#通过链接文本获取对象
button=broswer.find_element(By.LINK_TEXT,'地图')
print(button)