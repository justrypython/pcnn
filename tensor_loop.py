#encoding:UTF-8

import numpy as np
import tensorflow as tf

def body(x):
    a = tf.random_uniform(shape=[2, 2], dtype=tf.int32, maxval=100)
    b = tf.constant(np.array([[1, 2], [3, 4]]), dtype=tf.int32)
    c = a + b
    return tf.nn.relu(x + c)

def condition(x):
    return tf.reduce_sum(x) < 100

def main():
    x = tf.Variable(tf.constant(0, shape=[2, 2]))
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        result = tf.while_loop(condition, body, [x])
        print result.eval()
        tf.summary.scalar('fake', 0)
        summary = tf.summary.merge_all()
        writer = tf.summary.FileWriter('./tmp', graph=sess.graph)
        writer.add_summary(sess.run(summary))
        writer.flush()
        
    print 'end'
    
if __name__ == '__main__':
    main()