# this script is to visualize and graph out pmon data. 

from pandas import read_csv
from matplotlib import pyplot
import os
import numpy as np

def loop_folders(stutter_yes_or_no):
    #change below to "Stutter" or "NoStutter"
    stutter_folder = f"Results\\False Negatives"

    directory = os.fsencode(stutter_folder)
        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        _ = create_plot(filename, stutter_folder, stutter_yes_or_no)
        if _ == "fail":
            print("fail")
            continue

def create_plot(csv_path, stutter_folder, stutter_yes_or_no):
    found = False
    try:
        dataset = read_csv(os.path.join(stutter_folder, csv_path), header=0)

        try:
            dataset = dataset[ ["TimeInSeconds", "Dropped", "MsBetweenPresents", "MsBetweenDisplayChange", "MsInPresentAPI", "MsUntilRenderComplete", "MsUntilDisplayed"]]
            found = True
            if dataset["MsUntilDisplayed"].dtype != np.number:
                return "fail"
            print("yes")

        except:
            dataset = dataset[ ["TimeInSeconds", "Dropped", "msBetweenPresents", "msBetweenDisplayChange", "msInPresentAPI", "msUntilRenderComplete", "msUntilDisplayed"]]
            found = True
            if dataset["msUntilDisplayed"].dtype != np.number:
                return "fail"
            print("yes1")

        if found == True :
            values = dataset.values

            groups = [0,1,2,3,4,5,6]

            i = 1
            pyplot.figure()

            for group in groups:
                pyplot.subplot(len(groups),1,i)
                pyplot.plot(values[:, group])
                pyplot.title(dataset.columns[group], y=0.5, loc='right')
                i+=1

            #pyplot.show()
            pyplot.savefig(os.path.join("Results", "False Negatives", "Visualized", csv_path) +".png")
    except:
        return "fail"

if __name__ == "__main__":
    stutter_yes_or_no = "NoStutter"
    loop_folders(stutter_yes_or_no)
