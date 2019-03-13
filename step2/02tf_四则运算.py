"""
第一次修改
"""
import tensorflow as tf
data1 = tf.constant(10)
data2 = tf.constant(20)
tfAdd = tf.add(data1,data2)
tfSub = tf.subtract(data1,data2)
tfMul = tf.multiply(data1,data2)
tfDiv = tf.divide(data1,data2)

#输出方式一(tf.Session()方式创建sess使用后需要关闭资源)
sess = tf.Session()
print(sess.run(tfAdd))
print(sess.run(tfSub))
print(sess.run(tfMul))
print(sess.run(tfDiv))
sess.close()
#输出方式二(sess使用后不需要关闭资源)
with tf.Session() as sess:
    print(sess.run(tfAdd))
    print(sess.run(tfSub))
    print(sess.run(tfMul))
    print(sess.run(tfSub))
"""
第二次修改
"""
import tensorflow as tf
second_data1 = tf.constant(10)
second_data2 = tf.Variable(15)
second_add = tf.add(second_data1,second_data2)
second_sub = tf.subtract(second_data1,second_data2)
second_mul = tf.multiply(second_data1,second_data2)
second_div = tf.divide(second_data1,second_data2)
init = tf.global_variables_initializer()    #变量在进行操作之前必须进行初始化
with tf.Session() as sess:
    sess.run(init)                             #变量的初始化也要通过sess进行运行
    print(sess.run(second_add))
    print(sess.run(second_sub))
    print(sess.run(second_mul))
    print(sess.run(second_div))

"""
第三次修改
"""
import tensorflow as tf
third_data1 = tf.constant(10)
third_data2 = tf.Variable(30)
third_add = tf.add(third_data1,third_data2)
# 完成当前的数据拷贝: 把当前third_add的结果追加到third_data2中
third_copy = tf.assign(third_data2,third_add)# third_add ->third_data2
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print("-------------------")
    # 将6和2相加的结果放到data2中
    print('sess.run(third_copy)',sess.run(third_copy))

    # 除过run方法还可以使用.eval()直接输出。eval方法相当于下面这句话
    # tf.get_default_session().run()
    print('third_copy.eval()',third_copy.eval())

    # 获取默认的session，执行run操作
    print('tf.get_default_session()',tf.get_default_session().run(third_copy))













