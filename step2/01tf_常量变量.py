
import tensorflow as tf
sess = tf.Session()
data1 = tf.constant(2,dtype=tf.int32)       # 常量，指定数据类型
data2 = tf.Variable(10,name="var")
data3 = tf.Variable(20,name="var1")         # 变量，指定变量名
print(data1)
print(data2)
print(data3)
print(f"data1:{sess.run(data1)}")          #常量不需要初始化

init = tf.global_variables_initializer()
sess.run(init)                              #变量需要初始化
print(f"data2:{sess.run(data2)}")
print(f"data3:{sess.run(data3)}")
sess.close()

'''
sess = tf.Session()
print(sess.run(data1))

# 这里可以正确打印出data1

init = tf.global_variables_initializer()
sess.run(init)

# 但是当我们仍要用这个sess打印data2时会报错
# 对于变量数值，我们要进行初始化。
print(sess.run(data2))
sess.close()
'''


""""
# 本质 tf = tensor + 计算图
# tensor 数据
# op 
# graphs 数据操作
# session
"""