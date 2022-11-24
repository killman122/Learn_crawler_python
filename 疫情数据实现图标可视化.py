import requests
import csv  # 内置模块用来保存数据,类似与excel文件
# import
i = 111
url = f'https://shiapp.huajiet.com/api.html?XDEBUG_SESSION_START=16315&X-CSRF-TOKEN={i}' # 格式化字符串
f=open('疫情数据cvs',mode='a',encoding='utf-8',newline='')

print(url)
