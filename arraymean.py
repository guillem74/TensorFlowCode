import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.Variable([10, 20, 30])


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(tf.reduce_mean(x)))

#For version 0.11 and earlier use: init_op = tf.initialize_all_variables()
#Instead of tf.global_variables_initializer()