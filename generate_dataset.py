# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:10:05 2019

@author: Timmy_Fan
"""
import numpy as np
#读取数据
def generate_dataset()
    train_data = np.loadtxt(open("train_data.txt","rb"),delimiter=",")  
    X = train_data[0:50000,0:23]
    Y = train_data[0:50000,23:24]
    test_data = np.loadtxt(open("test_data.txt","rb"),delimiter=",")  
    X_test = test_data[0:50000,0:23]
    Y_test = test_data[0:50000,23:24]
    return X,Y,X_test,Y_test