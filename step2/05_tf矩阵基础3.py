import tensorflow as tf

#全0矩阵
mat0 = tf.zeros([2,3])
#全1矩阵
mat1 = tf.ones([2,3])
#填充矩阵
mat2 = tf.fill([2,3],15)
#全0相似矩阵
mat = tf.constant([[2],[3],[4]])    #3行1列
mat_like0 = tf.zeros_like(mat)
#全1相似矩阵
mat_like1 = tf.ones_like(mat)
# 将0-2之间数据分成相等的10份，中间有10个数据，要填11
mat_linspace = tf.linspace(0.0,2.0,11)
# 随机数矩阵，2行三列，数字为-1到2之间的随机数
mat_random_uniform = tf.random_uniform([2,3],-1,2)
with tf.Session() as sess:
    # print(sess.run(mat0))
    # print(sess.run(mat1))
    # print(sess.run(mat2))
    # print(sess.run(mat_like0))
    # print(sess.run(mat_like1))
    print(sess.run(mat_linspace))
    print(sess.run(mat_random_uniform))

