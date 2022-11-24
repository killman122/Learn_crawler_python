import itchat,time
itchat.login()#登录微信
#itchat.auto_login(hotReload=True)
#mps=itchat.get_mps()
account=itchat.get_friends()
print(account)