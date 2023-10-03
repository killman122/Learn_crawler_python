# 定义的一个修改之前的字典
person = {'name': '法外狂徒', 'age': 18}

print(person['name'])
# 这里不能使用get的方式修改数据应为get是获取数据而非修改数据
# person.get('name')='法外狂徒'
# 修改name的值为法外狂徒
person['name']='狂徒'

print(person.get('name'))
# 显示为法外狂徒修改成功
