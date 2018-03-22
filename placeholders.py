import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



x = tf.placeholder("float")
y = tf.placeholder("float")
z = tf.multiply(x, y)

#You typically load feed_dict from a data foler, etc
#This is only made for giving an example
feed_dict = {x:5,y:6}

#Run the session using with block (automatically closes)

with tf.Session() as sess:
    print(sess.run(y, feed_dict))