import urllib.request
import urllib.parse
import http.cookiejar
import time
# 使用cookiejar获取网页的cookie
# import http.cookiejar, urllib.request  

# cookie = http.cookiejar.CookieJar()  
# handler = urllib.request.HTTPCookieProcessor(cookie)  
# opener = urllib.request.build_opener(handler)  
# response = opener.open('http://www.baidu.com')  
# for item in cookie:  
#     print(item.name+"="+item.value)

# print((cookie),type(cookie))
# time.sleep(2)

import requests  

r = requests.get('https://www.baidu.com/')    
print(r.cookies)
for i in r.cookies:
    print(i)

for key, value in r.cookies.items():
    print(key + '=' + value)