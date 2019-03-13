import tensorflow as tf
data1 = tf.constant([[6,6]])
data2 = tf.constant([[2],
                     [2]])
data3 = tf.constant([[3,3]])
data4 = tf.constant([[1,2],
                    [3,4],
                    [5,6]])
print(type(data4))                          #<class 'tensorflow.python.framework.ops.Tensor'>
print(type([[1,2],[2,3]]))                  #<class 'list'>
matMul = tf.matmul(data1,data2)             #矩阵乘法[m*k]*[k*n]=[m*n]
matMul2 = tf.multiply(data1,data2)          #普通乘法[m*k]*[k*n]=[k*k]
matAdd = tf.add(data1,data3)                #矩阵加法[m*n]+[m*n]=[m*n]
with tf.Session() as sess:
    print(sess.run(matMul))
    print(sess.run(matAdd))
    print(sess.run([matMul,matAdd,matMul2]))    #输出时需要用([])，不然会报错
    # 输出： [array([[24]]),
    #         array([[9, 9]]),
    #         array([[12, 12],
    #         [12, 12]])]

