#this file is for predicting; it is called by main and used to predict on a single csv
#both heuristic and ML approach will be in this file

import numpy as np
from keras import backend as K
import preprocessing_functions as func
import pickle

def rules(frames, spike, freq):
    #taken from seans realtimestutterdetection.py
    #frames = frames.sort_values(ascending=True)
    frames.sort()

    spikesbyframes = freq
    spikefactor = spike

    total = len(frames)
    n50th = round(total*0.50)
    # majorspikes = 0    
    # bighits = 0
    # hits=0

    spike_counter = 0
            
    temp = frames[n50th] * spikefactor#looky here
    for x in range(n50th,len(frames)):
        if frames[x] > temp:
            spike_counter +=1
        
    # print("Spikes: "+str(spike_counter))
    # if spike_counter>0:
    #     majorspikes += 1

    ''' 
    if spike_counter/len(frames)>spikesbyframes:
        hits += 1
        badfiles[key] += 1
        if spike_counter/len(frames)>spikesbyframes:
            bighits += 1
    '''            
    #print("--------------------------------------------------------")
    #print("--------------------------------------------------------")
    #print("All Stutter Success Rate:"+str((hits/fcount)*100))
    #print("Major Stutter Success Rate:"+str((bighits/majorspikes)*100))
    #print("--------------------------------------------------------")
    
    #r["ASSR"] = (hits/fcount)*100
    if (spike_counter/total) >= spikesbyframes:
        return True
    else:
        return False


def ml(data_list, max_length, model, threshold, bias = None):
    data_list = pre_predict(data_list, max_length)
    pred = model.predict(data_list)
    # print(pred[0][0])
    if bias:
        if pred[0][0]>bias:
            return True

    if pred[0][0]>threshold:
        return True
    else:
        return False

#this function mostly does the same as the data preprocessing. we need to apply the same
#data processing for prediction
def pre_predict(data_list, max_length):
    #pickle from our preprocessing. needs to be the same one
    with open ('Pickles/scaler.ob', 'rb') as fp:
        scaler = pickle.load(fp)

    data_list = func.padding_x([data_list], max_length)
    data_list = func.alter_spike(data_list, 100, 1.5)
    data_list = func.standardize_all(data_list, max_length, scaler)
    data_list = np.array(data_list)
    data_list = np.reshape(data_list, (-1, max_length ,1))

    return data_list

#functions to calculate metrics about the model
def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))