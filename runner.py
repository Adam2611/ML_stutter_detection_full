#This file is an example of how to run main.py from another file. 
#27.csv has no stutter fyi

import main


prediction = main.main_predict("27.csv")

if prediction:
    print("Stutter!")
else:
    print("No Stutter!")