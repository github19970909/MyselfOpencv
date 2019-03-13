# import tensorflow as tf
# data1 = tf.placeholder(tf.float32)
# data2 = tf.placeholder(tf.float32)
# dataAdd = tf.add(data1,data2)
# with tf.Session() as sess:
#     s = sess.run(dataAdd,feed_dict={data1:2,data2:6})
#     print(s)

import tensorflow as tf
sedata1 = tf.constant([6,6])
sedata2 = tf.constant([[2],
                       [2]])
sedata3 = tf.constant([[1,2],
                       [3,4],
                       [5,6]])
print(sedata3.shape)                    #维度 (3, 2)
with tf.Session() as sess:
    print(sess.run(sedata3[0]))         #打印第一行
    print(sess.run(sedata3[:,0]))       #打印第一列
    print(sess.run(sedata3[0,0]))       #打印第一行第一列
