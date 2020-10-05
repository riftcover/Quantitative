n =int(input("请输入一个大于0的整数:"))
mysum = 0
num = 1
while num<=n :
    mysum= mysum + num
    num +=1
print("1加到 %d 的和为：%d" % (n,mysum))
