import time
import document
from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# path='msedgedriver.exe'
# broswer=webdriver.Edge(path)
path = r"msedgedriver.exe"  # 在绝对路径前加r防止字符串转义,但是注意检查浏览器的版本edgewebdriver版本和下载的msedge是否一致不一致会产生问题
# executable_path=driver_url
broswer = webdriver.Edge(path)

url = 'https://space.bilibili.com/1352889584/fans/follow?spm_id_from=333.1007.0.0'
broswer.get(url)
broswer.maximize_window()
time.sleep(3)
button = broswer.find_element(By.XPATH, '//div[@class="unlogin-avatar"]')
button.click()
# time.sleep(4)

# input=broswer.find_element(By.XPATH,'//div//input[@placeholder="请输入账号"]')
# input.send_keys()
# broswer.delete_all_cookies()
time.sleep(25)
'''
broswer.add_cookie({'name': '_uuid', 'value': 'F1C73EA5-6BF9-B466-6790-7DABE6C3689C16513infoc'})
broswer.add_cookie({'name': 'buvid3', 'value': '288976E6-E385-4A5B-AC35-3290B3435C58148826infoc'})
broswer.add_cookie({'name': 'PVID', 'value': '1'})
broswer.add_cookie({'name': 'buvid_fp_plain', 'value': '288976E6-E385-4A5B-AC35-3290B3435C58148826infoc'})
broswer.add_cookie({'name': 'rpdid', 'value': "|(um~u)R~)lk0J'uYJkJmmRYJ"})
broswer.add_cookie({'name': 'LIVE_BUVID', 'value': 'AUTO9516325717331533'})
broswer.add_cookie({'name': 'video_page_version', 'value': 'v_old_home'})
broswer.add_cookie({'name': 'buvid4', 'value': '87A3B33F-8B55-8470-9ACA-5D183A75950B58299-022012518-Vvnd5zdoRgEqKHUNBM8nkg%3D%3D'})
broswer.add_cookie({'name': 'buvid_fp', 'value': 'e1a709af451ffaa633ceaf44bc7dfb7f'})
broswer.add_cookie({'name': 'i-wanna-go-back', 'value': '-1'})
broswer.add_cookie({'name': 'CURRENT_BLACKGAP', 'value': '0'})
broswer.add_cookie({'name': 'fingerprint', 'value': '5d4f5c98fae895801be9b9bce7dea49d'})
broswer.add_cookie({'name': 'DedeUserID', 'value': '1352889584'})
broswer.add_cookie({'name': 'DedeUserID__ckMd5', 'value': 'e7c30eaf4157d4ee'})
broswer.add_cookie({'name': 'nostalgia_conf', 'value': '-1'})
broswer.add_cookie({'name': 'b_ut', 'value': '5'})
broswer.add_cookie({'name': 'hit-dyn-v2', 'value': '1'})
broswer.add_cookie({'name': 'blackside_state', 'value': '0'})
broswer.add_cookie({'name': 'CURRENT_QUALITY', 'value': '80'})
broswer.add_cookie({'name': 'bili_jct', 'value': '253cfdd8e15365fbe7c8b200512ec0d5'})
broswer.add_cookie({'name': 'CURRENT_FNVAL', 'value': '4048'})
broswer.add_cookie({'name': 'bp_video_offset_1352889584', 'value': '686474033209802800'})
broswer.add_cookie({'name': 'b_lsid', 'value': '7E4C7D10F_18232DC74A6'})
broswer.add_cookie({'name': 'b_timer', 'value': '%7B%22ffp%22%3A%7B%22333.999.fp.risk_288976E6%22%3A%2218232DC7B14%22%2C%22333.788.fp.risk_288976E6%22%3A%2218232DC91D5%22%2C%22333.880.fp.risk_288976E6%22%3A%2218232E94699%22%7D%7D'})
broswer.add_cookie({'name': 'sid', 'value': '8fb4pmac'})
'''
# broswer.get(url)
# time.sleep(10)

button = broswer.find_element(By.XPATH, '(//li[@title="3"])[1]')  # 移动到第三页
button.click()
time.sleep(3)

button = broswer.find_element(By.XPATH, '(//li[@title="5"])[1]')  # 移动到第五页
button.click()
time.sleep(4)

# down=i.find_element(By.XPATH,'//div[@class="fans-action"]//div[@class="be-dropdown fans-action-btn fans-action-follow"]//ul//li[2]')
# ActionChains(broswer).move_to_element(down).perform()
drop_down = broswer.find_elements(By.XPATH,
                                  '//div[@class="be-dropdown fans-action-btn fans-action-follow"]')  # 这里是将鼠标定位
drop_item = broswer.find_elements(By.XPATH,
                                  '//div[@class="fans-action"]//div[@class="be-dropdown fans-action-btn fans-action-follow"]//ul')
button = broswer.find_element(By.XPATH, '(//li[@title="上一页"])[1]')  # 移动到下一页


# button.click()
# global act
def f():
    for i in range(len(drop_down)):
        print(i)
        down = drop_down[i]
        item = drop_item[i]
        ActionChains(broswer).move_to_element(down).perform()
        # act=ActionChains(broswer).move_to_element(down).perform()
        time.sleep(1)
        # act=ActionChains(broswer).move_to_element_with_offset(item,20,-34)
        ActionChains(broswer).click(broswer.find_element(By.XPATH,'//div[@class="fans-action"]//div[@class="be-dropdown fans-action-btn fans-action-follow"]//ul//li[2]')).perform()
        # time.sleep(2)
        # act.click()
        # act.click()
        time.sleep(3)
        # 滑倒页面底部
        # js_button='document.documentElement.scrollTop=100'
        # broswer.execute_script(js_button)
        # time.sleep(2)
        if i == 19:
            button.click()
            time.sleep(8)
    return f()


f()
button = broswer.find_element(By.XPATH, '(//li[@title="5"])[1]')  # 移动到第五页
button.click()
time.sleep(4)

# ActionChains(broswer).move_to_element(broswer.find_element(By.XPATH,'//div[@class="fans-action"]//div[@class="be-dropdown fans-action-btn fans-action-follow"]//ul')).perform()
# time.sleep(6)
# for x in range(len(name_list)):
#    print(x)
#    name=name_list[x]
#    src=img_list[x]
# i.click()
# time.sleep(2)
# print(i,type(i))
# choice=i.find_element(By.XPATH,'//li[contains(text(),"取消关注")]')
# print(choice)
# choice.


# btn=broswer.find_element(By.XPATH,"")
# ActionChains(broswer).move_to_element(broswer.find_elements(By.XPATH,'//span[@class="fans-action-text"]').perform()
# set=broswer.find_elements(By.XPATH,'//span[@class="fans-action-text"]')
# for mouse in set:

# button_list=broswer.find_elements(By.XPATH,'//li[contains(text(),"取消关注")][1]')
# for button in button_list:
#    #print(button.accessible_name)
#    #print(button,type(button))
#    #button.click()
#    time.sleep(2)
# button.click()
# time.sleep(4)


'''
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
'''
