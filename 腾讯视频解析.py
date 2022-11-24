"""
value="https://www.ckmov.vip/api.php?url="
value="https://www.1717yun.com/jx/ty.php?url="
value="http://okjx.cc/?url="
value="https://z1.m1907.cn/?jx="
value="https://ckmov.ccyjjd.com/ckmov/?url="
https://123.1dior.cn/?url=
https://www.murl.us/?url=
value="https://www.h8jx.com/jiexi.php?url="
https://vip.fxw.la/m3u8/index.php?url=
"""

import requests
import re
import tkinter as tk#GUI窗口
import webbrowser#导入用来打开网站

v1="https://www.ckmov.vip/api.php?url="
v2="https://www.1717yun.com/jx/ty.php?url="
v3="http://okjx.cc/?url="
v4="https://z1.m1907.cn/?jx="
v5="https://ckmov.ccyjjd.com/ckmov/?url="
#v6="https://123.1dior.cn/?url="
v7="https://www.murl.us/?url="
v8="https://www.h8jx.com/jiexi.php?url="
m3u8="https://vip.fxw.la/m3u8/index.php?url="

root=tk.Tk()#实例化对象父窗口
root.title('视频解析')
root.geometry('600x400')
l1=tk.Label(root,text='播放接口',font=12)#将组件绑定在root父窗口上
l1.grid()

var=tk.StringVar()#设置一个字符串变量
#value的值会传给variable     variable=var
b1=tk.Radiobutton(root,text='播放接口1',variable=var,value=v1)
b1.grid(row=0,column=1)
b2=tk.Radiobutton(root,text='播放接口2',variable=var,value=v2)
b2.grid(row=1,column=1)
b3=tk.Radiobutton(root,text='播放接口3',variable=var,value=v3)
b3.grid(row=2,column=1)
b4=tk.Radiobutton(root,text='播放接口4',variable=var,value=v4)
b4.grid(row=3,column=1)
b5=tk.Radiobutton(root,text='播放接口5',variable=var,value=v5)
b5.grid(row=4,column=1)
#b6=tk.Radiobutton(root,text='播放接口6',variable=var,value=v6)
#b6.grid(row=5,column=1)
b7=tk.Radiobutton(root,text='播放接口7',variable=var,value=v7)
b7.grid(row=6,column=1)
b8=tk.Radiobutton(root,text='播放接口8',variable=var,value=v8)
b8.grid(row=7,column=1)
b9=tk.Radiobutton(root,text='m3u8x',variable=var,value=m3u8)
b9.grid(row=8,column=1)

l2=tk.Label(root,text='解析链接:',font=12)
l2.grid(row=10,column=0)

#文本输入框单行
t1=tk.Entry(root,width=55)
t1.grid(row=10,column=1)

def bf():
    webbrowser.open_new(var.get()+t1.get())#get实现了获取var中的内容以t1文本框中的内容

def clear():
    t1.delete(0,'end')

btn1=tk.Button(root,text='播放▶',font=9,command=bf)
btn1.grid(row=11,column=1)
btn2=tk.Button(root,text='清除',font=9,command=clear)
btn2.grid(row=12,column=1)



root.mainloop()#主函数循环刷新出现窗口





'''
url='https://v.qq.com/'
response=requests.get(url)
print(response)
response.encoding='utf-8'
#response.apparent_encoding 自动识别转化
response=response.text
#result=response.decode('utf-8')
print(response)
reg=re.compile('')
res=re.findall(reg.response)
#正则表达式中加入?为了防止贪婪匹配直接从开始位置匹配到结束位置的所有
#使用reg规则在response响应中取
#正则中取出的是列表


pyinstaller -F -w xxx.py
'''