tup1 = ("book" , "desk","bag",2000,2008,2012,2015, 2018)
#使用下标索引来访问元组中的值
print ("元组中的第二个值，tup1[1]: ", tup1[1])
#使用中括号的形式截取字符
print ("元组中的第二和第五个值，tup1[1:5]: ", tup1[1:5])
#利用for循环语句来遍历元组中的值
print("利用for循环语句来遍历元组中的值")
for i in tup1:
    print(i)
#连接元组
tup2 =("Python","Baidu")
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)
#删除元组
del tup3
print ("删除后的元组 tup  ")
