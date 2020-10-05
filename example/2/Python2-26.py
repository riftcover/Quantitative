def  myprint() :         #自定义函数，实现输出Python，您好！
   print("Python,您好！")
def myarea(x1,x2):       #自定义函数，实现三角形的面积计算
    return 1/2*x1*x2
myprint()   #调用自定义函数myprint()
#调用自定义函数myarea()
w = 12
h = 6
print("三角形的底 =", w, " 三角形的高 =", h, " 三角形的面积 =", myarea(w, h))
