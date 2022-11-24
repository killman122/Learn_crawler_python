#此处的异常方法与在脚本编写中报的try...except exception类型相同
fp=open('text.txt','r')
fp.read()
fp.close()

#异常的格式
#try:
    #可能出现异常的代码
#except #异常的类型
#    友好的提示
try:
    fp=open('text.txt','r')
    fp.read()
except FileNotFoundError:
    print('系统正在升级,请稍后再试')