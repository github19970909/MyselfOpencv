import cv2
# 读取图片
img = cv2.imread("image0.jpg",1)

# 第一个参数: 图片名称
# 第二个参数: 图片的原始数据
# 第三个参数: 图片的质量(0-100)
cv2.imwrite("my_firstQulity.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,50])
# 1M 100k(正常) 10k(模糊) 0-100 有损压缩（以牺牲图片质量为代价）

