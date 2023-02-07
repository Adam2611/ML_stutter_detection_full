#main driver program
#this is the main file for predictions. It takes in a file path and returns the prediction of that file. 
#might need to rename this fyi if causing conflicts

#!!!
#LOOK AT LINE 43 ish for returning a result if using for production!!!!
#!!!

import os
import pandas as pd
import predict
import preprocessing_functions as func
from tensorflow import keras

def main_predict(file_path = None):
    max_length = 15000
    freq = 0.0021  #0.0001 - 0.001; 0.00002
    spike = 3.7 #1.9-8.9; 0.2
    model = create_model() #make sure to put the right string in the create_model function
    threshold = 0.75

    #put the path of the file/directory we want to be predicted here
    if file_path:
        prediction_path = file_path 
    else:
        prediction_path = os.path.join("StutterData", "test", "Imbalanced_yes")

    #for single files:
    
    prediction = test_predictions((prediction_path), spike, freq, max_length, model, threshold)
    #if in production and testing single files
    return prediction

    #for multiple files in a directory:
    # directory = os.fsencode(prediction_path)
    # prediction_list = []
    # count = 0
    # bad_count = 0
    
    # for file in os.listdir(directory):
    #     filename = os.fsdecode(file)
    #     prediction = test_predictions(os.path.join(prediction_path, filename), spike, freq, max_length, model, threshold)
    #     prediction_list.append(prediction)
   
    #real world inference
    # for pred in prediction_list:
    #     if pred == True:
    #         count+=1
    #     else:
    #         bad_count+=1

    # print("Right: ", count)    
    # print("Wrong: ", bad_count)    
    # print("Percent: ", float(count/(count+bad_count)))

def test_predictions(path, spike, freq, max_length, model, threshold):
    try:
        dataset = pd.read_csv(path, header=0, usecols=["MsBetweenPresents"], dtype = {"MsBetweenPresents":float})
        data_list = dataset["MsBetweenPresents"].tolist()

    except:
        dataset = pd.read_csv(path, header=0, usecols=["msBetweenPresents"], dtype = {"msBetweenPresents":float})
        data_list = dataset["msBetweenPresents"].tolist()

    # stutter_guess = False
    data_list1 = data_list.copy()
    data_list2 = data_list.copy()
    
    
    stutter_guess=predict.rules(data_list1, spike, freq)
    
    if stutter_guess==True:
        stutter_guess2=predict.ml(data_list2, max_length, model, threshold, bias=0.65)
        if stutter_guess2==True:
            return True
        else:
            return False

    else:
        stutter_guess3=predict.ml(data_list, max_length, model, threshold)
        return stutter_guess3

def create_model():
    dependencies = {
    'f1_m': predict.f1_m,
    'precision_m': predict.precision_m,
    'recall_m': predict.recall_m
    }
    model = keras.models.load_model('best_model_10_current.h5', custom_objects=dependencies)
    return model


if __name__ == "__main__":
    main_predict()    
