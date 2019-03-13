# imread:参数1: 图片的名称，参数2: 图片的类型。
# 0 gray灰度图片 1 彩色图片 ；返回当前图片内容
import cv2
img = cv2.imread('image0.jpg',1)
# imshow-->参数1: 窗体名称, 参数2: 要展示的图片内容
cv2.imshow('my_firstImg.jpg',img)
# 程序stop
cv2.waitKey (0)


# 1 文件的读取 2 封装格式解析 3 数据解码 4 数据加载
# 2,3 步骤是opencv内部帮我们做的
# img = cv2.imread('image0.jpg',1)
# cv2.imshow('image',img)
# 图片格式: jpg png（文件的封装格式）；
# 文件会由两部分组成:
# 1 文件头: 数据部分的解码信息和附加信息
# 2 文件数据（不指图片原始数据，而指图片进行压缩编码之后的数据）
# 解码器根据解码信息和附加信息将图像还原成原始数据
