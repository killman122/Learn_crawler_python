import time
import document
from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains #导入动作链对象

# path='msedgedriver.exe'
# broswer=webdriver.Edge(path)
path = r"msedgedriver.exe"  # 在绝对路径前加r防止字符串转义,但是注意检查浏览器的版本edgewebdriver版本和下载的msedge是否一致不一致会产生问题"D:\msedgedriver.exe"
# executable_path=driver_url
broswer = webdriver.Edge(path)

url = 'https://www.baidu.com'
broswer.get(url)
broswer.maximize_window()

broswer.quit()  # 关闭浏览器

broswer.find_element(By.CSS_SELECTOR)
# 保存验证码图片可以使用.screenshot('filename')的方法实现,使用cssselect中的使用方法就是css语法,类选择器,id选择器等等

ActionChains(broswer).move_to_element_with_offset(a,x,y).click().perform()# 指定页面坐标元素执行操作  三个参数第一个参数是元素对象,第二个第三个是坐标值,click是点击,perform是执行动作链对象
ActionChains(broswer).move_to_element().perform()