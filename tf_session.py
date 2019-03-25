import tensorflow as tf


martix1=tf.constant([[3,3]])
martix2=tf.constant([[2],
                     [2]])

product=tf.matmul(martix1,martix2)  #martix multiply np.dot(m1,m2)

#method 1

#  sess=tf.Session()
# result=sess.run(product)
# sess.close()

#method 2
with tf.Session() as sess:
    print(sess.run(product))

