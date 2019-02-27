# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:09:05 2019

@author: Timmy_Fan
contact me :fk_Timmy_Avengers@163.com
"""
#define the process of forward spreading 
import tensorflow as tf
IMAGE_SIZE=480
NUM_CHANNELS=1
CONV1_SIZE=5
CONV1_KERNEL_NUM=32
CONV2_SIZE=5
CONV2_KERNEL_NUM=64
FC_SIZE=               #第一层全连接网络
OUTPUT_NODE=           #第二层全连接网络
#get weight parameters via this function with regularizer
def get_weight(shape,regularizer):
    w=tf.Variable(tf.truncated_normal(shape,dtype=tf.float64,seed=1,stddev = 0.1))
    if regularizer!=None : tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w
#get bias parameters via this function
def get_bias(shape):
    b=tf.Variable(tf.truncated_normal(shape,dtype=tf.float64,seed=1))
    return b
#
def conv2d(x,w)        #x--input descriprtion [,,,]4d      w--kernel description[,,,]4d
    return tf.nn.conv2d(x,w,strides = [1,1,1,1],padding = 'SAME')
def max_pool(x)        #x--input descriprtion [,,,]4d  
    return tf.nn.max_pool(x,ksize = [1,,,1],strides[1,2,2,1],padding = 'SAME')
#establish the structure of DNN with default 6 layers
def forward(x,train,regularizer):
    conv1_w = get_weight([CONV1_SIZE,CONV1_SIZE,NUM_CHANNELS,CONV1_KERNEL_NUM],regularizer)
    conv1_b = get_bias([CONV1_KERNEL_NUM])
    conv1   = conv2d(x,conv1_w)
    relu1   = tf.nn.relu(tf.nn.bias_add(conv1,conv1_b)) 
    pool1   = max_pool(relu1)
    
    conv2_w = get_weight([CONV2_SIZE,CONV2_SIZE,NUM_CHANNELS,CONV2_KERNEL_NUM],regularizer)
    conv2_b = get_bias([CONV2_KERNEL_NUM])
    conv2   = conv2d(x,conv2_w)
    relu2   = tf.nn.relu(tf.nn.bias_add(conv2,conv2_b)) 
    pool2   = max_pool(relu2)
    
    pool_shape = pool.get_shape().as_list()
    nodes = pool_shape[1]*pool_shape[2]*pool_shape[3]
    reshaped = tf.reshape(pool2,[pool_shape[0],nodes])
    
    w1 = get_weight([nodes,FC_SIZE],regularizer)
    b1 = get_bias(FC_SIZE)
    f1 = tf.nn.relu(tf.matmul(reshaped,w1) + b1)
    if train :  f1 = tf.nn.dropout(f1,0.5)
    
    w2 = get_weight([FC_SIZE,OUTPUT_NODE],regularizer)
    b2 = get_bias([OUTPUT_NODE])
    y_pre = tf.matmul(f1,w2) + b2
    return y_pre
    '''
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
    '''
#other activate functions: tf.nn.sigmoid(),tf.nn.tanh(),tf.nn.softmax()
#other parameters generate function tf.random_normal(),tf.random_uniform()
