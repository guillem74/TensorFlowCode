import tensorflow as tf
from random import randint
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


try:
    number1 = int(raw_input('Enter one number:'))
except ValueError:
    print "Not a number"

try:
    number2 = int(raw_input('Enter another number:'))
except ValueError:
    print "Not a number"

constant1 = [number1]
constant2 = [number2]

a = tf.constant(constant1)
b = tf.constant(constant2)

operation = randint(0, 3)

if operation == 0:
    print("Sum of both numbers is:")
    c = tf.add(a, b)
if operation == 1:
    print("Subtraction of both numbers is:")
    c = tf.subtract(a, b)
if operation == 2:
    print("Multiplication of both numbers is:")
    c = tf.multiply(a, b)
if operation == 3:
    print("Division of both numbers is:")
    c = tf.div(a,b)

with tf.Session() as session:
    result = session.run(c)
    print(result)