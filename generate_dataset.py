# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:10:05 2019

@author: Timmy_Fan
"""
import numpy as np
#loading dataset
def generate_dataset()
    train_data = np.loadtxt(open("train_data.txt","rb"),delimiter=",")  
    X = train_data[0:i,0:j] #i is the number of samples in your dataset and j is the number of features in your dataset
    Y = train_data[0:i,j:j+1] 
    test_data = np.loadtxt(open("test_data.txt","rb"),delimiter=",")  
    X_test = test_data[0:i,0:j]
    return X,Y,X_test
