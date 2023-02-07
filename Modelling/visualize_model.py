# this file is to graph the model results. 

import os
import matplotlib.pyplot as plt

def loop():
    model_folder = os.path.join("Results", "Model_results")

    directory = os.fsencode(model_folder)
        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if ".txt" in filename:
            cleaned = filename.split(".txt")[0]
            path = os.path.join(model_folder, cleaned+".png")
            # print(path)
            if not os.path.exists(path):
                with open(os.path.join(model_folder, filename)) as f:
                    lines = f.readlines()

                make_chart(lines)
                f.close()

def make_chart(lines):
    model_num = str(lines[0])
    model_num = str(model_num).split(":")[0]
    print(model_num)
    lines.pop(0)
    #graph will have 4 lines - 4 lists
    # stutter percent all
    # nonstutter percent all
    # stutter percent test
    # non stutter percent test
    stutter_all = []
    nonstutter_all = []
    stutter_test = []
    nonstutter_test = []

    index = 0
    for _ in range(9):
        stutter = lines[index+5]
        stutter_score = str(stutter).split(": ")[-1]
        nonstutter = lines[index+6]
        nonstutter_score = str(nonstutter).split(": ")[-1]
        stutter_all.append(float(stutter_score)*100)
        nonstutter_all.append(float(nonstutter_score)*100)
        index+=8

    for _ in range(9):
        stutter = lines[index+5]
        stutter_score = str(stutter).split(": ")[-1]
        nonstutter = lines[index+6]
        nonstutter_score = str(nonstutter).split(": ")[-1]
        stutter_test.append(float(stutter_score)*100)
        nonstutter_test.append(float(nonstutter_score)*100)
        index+=8

    plt.rcParams["figure.autolayout"] = True
    thresh = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    default_x_ticks = range(len(thresh))
    plt.plot(default_x_ticks, stutter_all, 'o-', color = "red", label='Stutter Percent All')
    plt.plot(default_x_ticks, nonstutter_all,'o-', color = "orange", label='NonStutter Percent All')
    plt.plot(default_x_ticks, stutter_test,'o-', color = "blue", label='Stutter Percent Test')
    plt.plot(default_x_ticks, nonstutter_test, 'o-',color = "green", label='NonStutter Percent Test')
    plt.xticks(default_x_ticks, thresh)
    plt.title(f"Correct Percents for {model_num} based on Confidence ", fontdict=None, loc='center', pad=None)
    plt.ylabel("Percent Correct", fontdict=None)
    plt.xlabel("Threshold/Confidence", fontdict=None)
    plt.legend()
    # plt.show()
    plt.savefig(os.path.join("Results", "Model_results", model_num) +".png")
    plt.clf()

if __name__ == "__main__":
    loop()