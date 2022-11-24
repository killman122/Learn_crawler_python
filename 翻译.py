import tkinter as tk
#使用tk.TK()可以生成一个软件的启动窗口
root=tk.Tk()

root.title('翻译软件')
root.geometry('400x200')#这里是设置窗体的大小
l1=tk.Label(root,text='请输入翻译内容:')#组件标签需要放在root窗口中
l1.grid()#将组件布局

t1=tk.Text(root,width=56,height=5)#将文本框标签绑定在root,一行56个字符,高度为五行
t1.grid()#摆放组件
t1.get(0,0,'end')#获取文本框中的内容,从第0行第0列开始到末尾
#删除文本框中的内容
t1.delete(0,0,'end')
#插入新结果到文本框text
t1.insert('end')#因为插入位置是空文本所以插入的起始位置等于插入的终止位置
#需要写三个按钮在窗体的布局上
b1=tk.Button(root,text='中文翻译',commend=fanyi)#这里的翻译相当于直接调用fanyi函数但是在此项目中我没有写函数

#一个组件只占一行,无论组件中设置了多少行
'''
请输入翻译内容:第0行
文本输入框text第一行
按钮第二行
'''
b1.grid(row=2,column=0)
b2=tk.Button(root,text='英文翻译')
b2.grid(row=3,column=0)
b3=tk.Button(root,text='清除')
b3.grid(row=4,column=0,width=8,commend=clear)#设置按钮的宽度等于8
root.mainloop()
#需要循环显示窗体否则只会显示出一次窗体
#这里是一个清除函数,清除函数中使用delete
def clear():
    t1.delete(0,0,'end')
"""
a='111'
b='111'
c='222'
if a=='111':
    print('1')
else:
    print(0)
"""