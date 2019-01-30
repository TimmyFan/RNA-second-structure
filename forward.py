# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:09:05 2019

@author: Timmy_Fan
contact me :fk_Timmy_Avengers@163.com
"""
#define the process of forward spreading 
import tensorflow as tf
#get weight parameters via this function with regularizer
def get_weight(shape,regularizer):
    w=tf.Variable(tf.truncated_normal(shape,dtype=tf.float64,seed=1))
    tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w
#get bias parameters via this function
def get_bias(shape):
    b=tf.Variable(tf.truncated_normal(shape,dtype=tf.float64,seed=1))
    return b
#establish the structure of DNN with default 6 layers
def forward(x,regularizer):
    w1 = get_weight(shape,regularizer)
    b1 = get_bias()
    f1 = tf.nn.relu(tf.matmul(x,w1) + b1)
    w2 = get_weight(shape,regularizer)
    b2 = get_bias())
    f2 = tf.nn.relu(tf.matmul(f1,w2) + b2)
    w3 = get_weight(shape,regularizer)
    b3 = get_bias()
    f3 = tf.nn.relu(tf.matmul(f2,w3) + b3)
    w4 = get_weight(shape,regularizer)
    b4 = get_bias()
    f4 = tf.nn.relu(tf.matmul(f3,w4) + b4)
    w5 = get_weight(shape,regularizer)
    b5 = get_bias()
    f5 = tf.nn.relu(tf.matmul(f4,w5) + b5)
    w6 = get_weight(shape,regularizer)
    b6 = get_bias()
    y_pre = tf.matmul(f5,w6) + b6
    return y_pre
#other activate functions: tf.nn.sigmoid(),tf.nn.tanh(),tf.nn.softmax()
#other parameters generate function tf.random_normal(),tf.random_uniform()
