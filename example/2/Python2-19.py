list1 = ["book" , "desk",2015, 2018]
#使用下标索引来访问列表中的值
print ("列表中的第一个值，list1[0]: ", list1[0])
#使用中括号的形式截取字符
print ("列表中的第三和第四个值，list1[2:4]: ", list1[2:4])
#利用for循环语句来遍历列表中的值
print("利用for循环语句来遍历列表中的值")
for i in list1:
    print(i)
#更新列表中的数据
print ("第三个元素为 : ", list1[2])
list1[2] = 2002
print ("更新后的第三个元素为 : ", list1[2])
list1.append("Baidu")
print ("更新后的列表 : ", list1)
#删除列表中的数据
print("没有删除元素之前的列表数据：",list1)
del list1[2]
print ("删除第三个元素之后的列表数据 : ", list1)

