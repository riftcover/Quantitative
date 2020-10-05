from math import log
def creatDataSet():
    # 数据集
    dataSet=[[0, 0, 0, 0, 'no'],
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']]
    #分类属性
    labels = ['年龄','有工作','有自己的房子','信贷情况']

    return dataSet,labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCouns ={}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCouns.keys():
            labelCouns[currentLabel]=0
        labelCouns[currentLabel]+=1

        shannonEnt=0.0

dataSet,features=creatDataSet()
cc = calcShannonEnt(dataSet)