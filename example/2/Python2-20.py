#列表中函数的应用
list1 = ["我","爱","python"]
list2 = [100, 200, 300,400]
print( "list1的最大值:", max(list1) )
print( "list2的最大值:", max(list2) )
print( "list1的最小值:", min(list1) )
print( "list2的最小值:", min(list2) )
print("list1的元数个数:",len(list1))
print("list2的元数个数:",len(list2))
 # id() 函数用于获取对象的内存地址
print("我的内存地址值：", id(list1[0]) )
print("爱的内存地址值：", id(list1[1]) )
print("python的内存地址值", id(list1[2]) )
aTuple = (123, 'Google', 'Runoob', 'Taobao')  #定义元组
list1 = list(aTuple)                          #把元组变成列表
print ("列表元素 : ", list1)
#列表中方法的应用
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)
list2.sort()
print ("list2列表排序后 : ", list2)
list2.reverse()
print ("list2列表反转后: ", list2)
list2.remove('Taobao')
print ("list2列表移除Taobao后 : ", list2)
list2.pop()
print ("list2列表再移除最后一个元素 : ", list2)
list2.insert(1, 'Runoob')
print ('列表插入元素后为 : ', list2)
print ('Runoob 索引值为', list2.index('Runoob'))
list2.clear()
print ("列表清空后 : ", list2)
