import tensorflow as tf

a = ([1, 2 , 3],
     [3, 2, 1],
     [2, 2, 2],
     [2, 10, 3])

x = tf.Variable(a)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(tf.argmax(x, 1)))


#argmax returns the index with the largest value across axis of a tensor.
#get tensor dimensions, In this case we are defining a 4 x 3 tensor.