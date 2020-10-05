num=int(input("输入一个数字："))
if num%2==0:
    if num%5==0:
        print ("输入的数字可以整除 2 和 5")
    else:
        print ("输入的数字可以整除 2，但不能整除 5")
else:
    if num%5==0:
        print ("输入的数字可以整除 5，但不能整除 2")
    else:
        print  ("输入的数字不能整除 2 和 5")
