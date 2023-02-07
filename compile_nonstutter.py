# for splitting of long non-stutter data (manually) collected
# this file takes in non-stutter data and preprocesses it. 
# input is several directories of different games with multiple pmon csvs. 
# output is one directory with pmon csvs capped at 30k rows and separated by game


import os
import pandas as pd

def compile():
    path1 = os.path.join("StutterData", "NoStutter_uncompiled", "Overwatch")
    directory1 = os.fsencode(path1)

    master_list = pd.DataFrame()
    names = []

    for file in os.listdir(directory1):
            filename = os.fsdecode(file)
            try:
                dataset = pd.read_csv(os.path.join(path1, filename), header=0, usecols=["MsBetweenPresents"], dtype = {"MsBetweenPresents":float})
                data_list = dataset["MsBetweenPresents"]
            except:
                dataset = pd.read_csv(os.path.join(path1, filename), header=0, usecols=["msBetweenPresents"], dtype = {"msBetweenPresents":float})
                data_list = dataset["msBetweenPresents"]

            data_list.drop(data_list.head(200).index, inplace=True)
            data_list.drop(data_list.tail(200).index, inplace=True)
            data_list.reset_index(drop=True)
            result = [master_list, data_list]
            temp_all = pd.concat(result)
            master_list = temp_all

    print(len(master_list))
    print(master_list.head())

    count = 0
    master_list = master_list.reset_index()
    master_list = master_list.drop("index", 1)
    master_list = master_list.rename(columns={0:"MsBetweenPresents"})
    print(master_list.head())
    # print(master_list.columns)
    # master_list.to_csv(f"StutterData/NoStutter_compiled/{count}.csv")

    while len(master_list) > 30000:
        size = len(master_list)
        sliced = master_list.iloc[size-30000:size]
        master_list = master_list.iloc[0:size-30000]
        sliced.columns = ["MsBetweenPresents"]
        sliced.to_csv(f"StutterData/NoStutter_compiled/{count}.csv")
        count+=1

    master_list.to_csv(f"StutterData/NoStutter_compiled/{count}.csv")

if __name__ == "__main__":
    compile()