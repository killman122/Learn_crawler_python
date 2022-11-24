# 一共三个逻辑运算符
# and not or
# 与或非
# and 全真才真   or全假才假 not 取非
print(10 >= 20 and 10 >= 11)

# not 非 取反
# t->f  f->t
print(not True)
print(not False)

# and 的性能优化 当and前面的结果是false的情况下,后面的代码就不再执行
# or的性能优化
a = 38
a > 39 or print('hello world')

# or的性能优化只要有一方为true那么结果就是true


# or 短路与 短路或
