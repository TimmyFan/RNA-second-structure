# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:09:36 2019

@author: Timmy_Fan
"""
import forward
import generate_dataset
import tensorflow as tf
BATCH_SIZE = 100
REGULARIZER = 0.01
learning_rate_base = 0.001
learning_rate_step = 1
learning_rate_decay = 0.99
STEPS = 50000
def backward():
    x = tf.placeholder(tf.float64,shape=(None,23))
    y_train = tf.placeholder(tf.float64,shape=(None,1))
    X,Y,X_test,Y_test = generate_dataset.generate_dataset()
    y_pred=forward.forward(x,REGULARIZER)
    global_step=tf.Variable(0,trainable=False)
    learning_rate = tf.train.exponential_decay(learning_rate_base,global_step,learning_rate_step,learning_rate_decay,staircase = False)
    mse = tf.reduce_mean(tf.square(y_pred-y_train))
    #cen = tf.nn.softmax_cross_entropy_with_logits(labels=y_train, logits=y_pre, name="cen")
    #average_loss = tf.reduce_mean(cen, name="average_loss")
    loss =  mse + tf.add_n(tf.get_collection('losses'))
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss,global_step = global_step)
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        #训练模型
        for i in range(STEPS):
            sess.run(train_step, feed_dict={x:X[0:20000], y_train:Y[0:20000]})
            if i%100 == 0:
                total_loss=sess.run(loss,feed_dict={x:X, y_train:Y})
                print(total_loss)  
                print(sess.run(y_pred,feed_dict={x:X, y_train:Y}))
if __name__ =='__main__':
    backward()

    