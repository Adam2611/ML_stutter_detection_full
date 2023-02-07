#tihs file is to optimize the algorithm
    # - we can optimize the heuristics by finding optimal spike and frequency
        # we essentially loop through the directories and slightly change the spike/frequency to find the best results
    # - we can optimize the model by changing the threshold and seeing the results
        # we essentially loop through the directories and slightly change the threshold to find the best results

import os
import pandas as pd
import predict
import main
import shutil

def optimize():
    #testing for optimal model
    # optimal_model()
    
    # testing for optimal heuristics
    optimal_heuristics()

def optimal_model():
    stutter_path = os.path.join("StutterData", "Stutter2")
    nostutter_path = os.path.join("StutterData", "NoStutter2")
    
    #optimizing model
    max_length = 15000
    model = main.create_model() #choose input file here
    
    # stutter_list = test_predictions(stutter_path, max_length=max_length, model=model, threshold=0.75)
    # nostutter_list = test_predictions(nostutter_path, max_length=max_length, model=model, threshold=0.75)

    for factor in range(40,85,5):
        threshold = factor/100
        stutter_list = test_predictions(stutter_path, max_length=max_length, model=model, threshold=threshold)
        nostutter_list = test_predictions(nostutter_path, max_length=max_length, model=model, threshold=threshold)
        call_results(stutter_list, nostutter_list, threshold=threshold)

    stutter_path = os.path.join("StutterData", "test", "Stutter_test")
    nostutter_path = os.path.join("StutterData", "test", "NoStutter_test")

    for factor in range(40,85,5):
        threshold = factor/100
        stutter_list = test_predictions(stutter_path, max_length=max_length, model=model, threshold=threshold)
        nostutter_list = test_predictions(nostutter_path, max_length=max_length, model=model, threshold=threshold)
        call_results(stutter_list, nostutter_list, threshold=threshold)


#this function is for finding optimal heuristics
def optimal_heuristics():
    # stutter_path = os.path.join("StutterData", "Stutter2")
    stutter_path = os.path.join("Results", "False Negatives")
    # nostutter_path = os.path.join("StutterData", "NoStutter2")
    nostutter_path = os.path.join("Results", "False Positives")
    stutter_list = []
    nostutter_list = []
    temp = 0 

    for spike in range(15, 99, 2):#0.2):
        print(spike/10)
        for freq in range(1, 40, 1):#0.00002):
            spike = spike/10
            freq = freq/10000
            nostutter_list = test_predictions(nostutter_path, spike, freq)
            for res in nostutter_list:
                if res == True:
                    temp+=1
            if temp>(len(nostutter_list)/10):
                stutter_list = []
                nostutter_list = []
                spike = spike*10
                freq = freq*10000
                temp = 0
                # print("continued")
                continue
            stutter_list = test_predictions(stutter_path, spike, freq)
            call_results(stutter_list, nostutter_list, spike, freq)
            stutter_list = []
            nostutter_list = []
            spike = spike*10
            freq = freq*10000
            temp = 0

            
#this file tests the stutter directories based on the predict.py module. 
def test_predictions(path, spike=None, freq=None, max_length = None, model = None, threshold=None):
    directory = os.fsencode(path)
    new_list = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        try:
            dataset = pd.read_csv(os.path.join(path, filename), header=0, usecols=["MsBetweenPresents"], dtype = {"MsBetweenPresents":float})
            data_list = dataset["MsBetweenPresents"].tolist()

        except:
            dataset = pd.read_csv(os.path.join(path, filename), header=0, usecols=["msBetweenPresents"], dtype = {"msBetweenPresents":float})
            data_list = dataset["msBetweenPresents"].tolist()

        if model:
            stutter=predict.ml(data_list,max_length,model, threshold)
        else:
            stutter=predict.rules(data_list, spike, freq)

        # if stutter == True:
        #     src = os.path.join(path, filename)
        #     dst = os.path.join("Results", "False Positives")
        #     shutil.copy(src, dst)
        new_list.append(stutter)
        
    return new_list

#this method tallies the stutter/nonstuter results and writes them to a file
def call_results(stutter_list, nostutter_list = None, threshold=None, spike=None, freq=None):
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0
    percent_stutter = 0
    percent_nonstutter = 0

    for x in stutter_list:
        if x == True:
            true_positive+=1
        else:
            false_negative+=1

    for y in nostutter_list:
        if y == False:
            true_negative+=1
        else:
            false_positive+=1

    percent_stutter = float(true_positive/(false_negative+true_positive))
    percent_nonstutter = float(true_negative/(false_positive+true_negative))

    f = open("Results/results5.txt", "a")
    f.write(f"""Spike: {spike}   Freq: {freq} Threshold: {threshold}\nTrue Positive: {true_positive} \nFalse Negative: {false_negative} 
True Negative: {true_negative} \nFalse Positive: {false_positive} \nPercent Stutter: {percent_stutter}
Percent Nonstutter: {percent_nonstutter}

""")
    print("written to!")



if __name__ == "__main__":
    optimize()    
