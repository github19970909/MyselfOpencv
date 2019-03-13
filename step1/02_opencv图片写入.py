# 1 图片名称 2 图片类型为1彩色图片 返回图片内容
import cv2
img = cv2.imread("image0.jpg",0)
# 参数1: 图片名称 参数2: 图片的数据(解码之后的图片原始数据)
cv2.imwrite("my_firstWriteImg.jpg",img) # 1 name 2 data
