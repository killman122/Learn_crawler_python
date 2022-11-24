import time
import document
from selenium import webdriver
from selenium.webdriver.common.by import *

#创建浏览器对象
path='msedgedriver.exe'
broswer=webdriver.Edge(path)

url='https://www.baidu.com'
broswer.get(url)

time.sleep(2)

#获取文本框的对象
input=broswer.find_element(By.ID,'kw')

#在文本框对象中写入值
input.send_keys('周杰伦')
time.sleep(3)

#点击按钮
button=broswer.find_element(By.ID,'su')
#print(button)<selenium.webdriver.remote.webelement.WebElement (session="a434a89402a8792ad6c055d9a932678a", element="6667289e-4423-41e9-a0c0-bab04e0ee41f")
print(button.accessible_name)
print(button.get_attribute('class'))#
button.click()
time.sleep(2)

#滑倒页面底部
js_button='document.documentElement.scrollTop=100000'
broswer.execute_script(js_button)
time.sleep(2)
#js="var q=document.documentElement.scrollTop=100000"  
#broswer.execute_script(js)  
#time.sleep(3)  

#点击第二页
button=broswer.find_element(By.XPATH,'//div[@id="page"]//span[contains(text(),"2")]')#获取span标签的内容为2的不是属性中的class或者是id
#print(button.accessible_name,button.tag_name,button.get_attribute('class'))
button.click()
time.sleep(3)

#回到上一页
broswer.back()

time.sleep(2)
#回到前面的一页
broswer.forward()
time.sleep(2)

#退出
#broswer.quit