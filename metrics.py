# this file provides metrics about the data and has other test functions


import os
import pandas as pd
import statistics
from sklearn import utils
#NonStutter2
# Median of length:  19254
# Average of length:  25533.97
#Stutter2
# Median of length:  17928
# Average of length:  24416.96
def test_shuffle():
    list1 = [ [10,10,10], [9, 9, 9], [8, 8, 8]]
    list2 = [ [0, 0, 0], [1, 1, 1], [0,0,0]]

    list1, list2 = utils.shuffle(list1, list2, random_state=10)

    print(list1)
    print(list2)

    combined = []
    combined=[list1, list2]

    combined = utils.shuffle(combined, random_state=10)

    print(combined[0])
    print(combined[1])

def length():
    path = os.path.join("StutterData", "NoStutter2")
    directory1 = os.fsencode(path)
    average = 0
    median = 0
    appends = []
    sum = 0
    i=0

    for file in os.listdir(directory1):
            filename = os.fsdecode(file)
            try:
                dataset = pd.read_csv(os.path.join(path, filename), header=0, usecols=["MsBetweenPresents"], dtype = {"MsBetweenPresents":float})
                data_list = dataset["MsBetweenPresents"].tolist()

            except:
                dataset = pd.read_csv(os.path.join(path, filename), header=0, usecols=["msBetweenPresents"], dtype = {"msBetweenPresents":float})
                data_list = dataset["msBetweenPresents"].tolist()

            appends.append(len(data_list))
            sum += len(data_list)
            i+=1
    median = statistics.median(appends)
    avg = float(sum/i)

    print("Median of length: ", median)
    print("Average of length: ", avg)

if __name__ == "__main__":
    length()