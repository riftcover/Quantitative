dict1 = {'姓名': '张平', '年龄': 12, '年级': '6','学习成绩':'优'}
for i,j in dict1.items():
    print(i, ":", j)
dict1['性别'] = '男'    #添加新的数据项
print ("添加数据项后字典是 : %s" %  dict1.items())
dict1['学习成绩'] = '及格'    #修改原有的数据项
print ("修改数据项后字典是 : %s" %  dict1.items())
del dict1['学习成绩']         #删除字典中的某一项数据
print ("删除某一项数据后字典是 : %s" %  dict1.items())
dict1.clear()                 #清空字典中所有数据项
print ("清空所有数据后字典是 : %s" %  dict1.items())
