import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([1,2,3,4,5,6,7,8])
# plot：折线   参数1：x坐标   参数2：y坐标     参数3：颜色     参数4：线宽
plt.plot(x,y,'g',lw=10)
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([15,20,10,22,6,8,9,10])
plt.bar(x,y,0.5,alpha=1,color='b')
plt.show()