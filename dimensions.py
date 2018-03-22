import tensorflow as tf

#The idea is to understand how dimensions are in Tensorflow
#s are scalars, v are vectors, m are matrices, t are tensors
#A tensor could be represented as matrices inside a bigger matrix

s = tf.Variable([1])
v1 = tf.Variable([1, 1])
v2 = tf.Variable([1, 1, 1])

m1 = tf.Variable([[1],
                  [1]])

m2 = tf.Variable([[1, 1],
                  [1, 1]])

m3 = tf.Variable([[1, 1, 1],
                  [1, 1, 1]])

m4 = tf.Variable([[1, 1 , 1],
                  [3, 2, 1],
                  [2, 2, 2]])

t1 = tf.Variable([[[1, 1]],
                  [[1, 1]]])

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(t1.get_shape)
