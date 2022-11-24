# 写数据
# write方法
'''
f=open('text.txt','w')
f.write('你好,世界 我在这'*5)
f.close()
'''
# 如果想要将字串换行需要加入转移字符\n来代替换行
# 在运行一次后会覆盖原有数据  如果文件存在  会先清空原来的数据 然后在重新写入
'''
f=open('text.txt','w')
f.write('你好,世界 我在这\n'*5)
f.close()
'''
# 如果我想在每一次执行之后都要追加数据,也就是说数据没有被覆盖而是将新的数据保存在原有的旧数据之下
f = open('text.txt', 'a')
f.write('你好,世界 我在这\n' * 5)
f.close()

# 读数据
# 默认情况下 read是一字节一字节的读取 效率比较低        读数据中的read()和readline()都是使用在文件的读取中如果不是本地文件则不需要使用
f = open('text.txt', 'r')
'''
content=f.read()
print(content)
'''
# 所以一般情况下不使用read一个字节一个字节的读取 采用readline一行一行的方式进行读取效率高 读取一行的方式对数据进行操作
'''
这种方式只读取一行
content=f.readline()
print(content)
'''
# 采用读取一行的方式读取完所有的数据
# readlines可以按照行来读取 但是会将所有的数据都读取到 并且以一个列表的形式返回 并且列表中的元素是一行一行的数据
content = f.readlines()
print(content)
