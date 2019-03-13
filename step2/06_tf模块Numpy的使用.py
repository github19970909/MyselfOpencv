import numpy as np

"""
【总结】
data2 = np.array([[1,2],[3,4],[5,6]])       #维度：(3, 2)
print(np.zeros([2,3]))                      #全0
data2[0,1] = 100                            #改查矩阵
无论是那种情况，在numpy的矩阵操作中，所有矩阵的形式都是由：最外层([ ])这是基础

"""


"""
初始化矩阵
"""
print("初始化矩阵")
data1 = np.array([1,2,3,4,5,6])             #维度：(6,)
data2 = np.array([[1,2],[3,4],[5,6]])       #维度：(3, 2)
data3 = np.array([[1,2,3]])                 #维度：(1, 3)
data4 = np.array([[1],[2],[3]])             #维度：(3, 1)
print(data1)
print(data2)
print(data3)
print(data4)
print(data1.shape,data2.shape,data3.shape,data4.shape)      #打印维度
"""
特殊矩阵
"""
print("特殊矩阵")
print(np.zeros([2,3]))                      #全0
print(np.ones([2,3]))                       #全1
"""
改查矩阵
"""
print("改查矩阵")
data2[0,1] = 100
print(data2[0,1],data2[0,0])
"""
矩阵基本运算(加减乘除)(此运算并不改变原有列表的值)
"""
print("矩阵基本运算")
caldata = np.ones([2,3])
print(caldata+2)
print(caldata-2)
print(caldata*2)
print(caldata/2)
"""
矩阵之间的操作(对应元素相加/相乘)
"""
data5 = np.array([[1,2],[3,4],[5,6]])
data6 = np.ones([3,2])
print(data5+data6)
print(data5*data6)