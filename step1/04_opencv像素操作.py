import cv2
img = cv2.imread("image0.jpg",1)

# 这里的img中存的图片数据是解析之后的。
# 读取具体的像素值。了解图片存储的坐标系结构
# 矩阵的x，y坐标值
(b,g,r) = img[100,100]          #将平面上100,100位置的像素点读取出来
print(b,g,r)

#现在如果想向图片中插入一条蓝色的线【(10,100)-->(110,100)在这一段上添加一条蓝色的线】
# 绘制一条直线
#10行 100列 --- 110行 100列结束
for i in range(10,110):
    img[i,100] = (0,0,255)      #在opencv中像素的值是按照bgr的形式存储与读取
cv2.imshow("my_firstPixelOperation",img)
cv2.waitKey(0)      #如果不给0，也可以给一个具体的整数1000 ms





