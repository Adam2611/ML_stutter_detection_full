#this file takes a directory of etw traces and turns them into pmon files;
#need all directories already set up and the pmon exe in the directory

import subprocess
import os

def etw_to_pmon():
    #enter the already made etw folder
    etw_folder = "StutterData\\ETW_Traces\\Stutter\\ETW_VOL"

    #enter the already made output folder
    converted_folder = "StutterData\\Stutter"
    """
    command to write in commandprompt:
    C:\\Users\\adamlam2\\Documents\\Code\\bloodhound_soln\\infrastructure\\Stutter_Detection>
    PresentMon-1.7.0-x64.exe -etl_file StutterData\\ETW_Stutter\\2021-12-06_22-23-15OW_StutterTear.etl -output_file converted\\testoutput.csv
    """

    directory = os.fsencode(etw_folder)
        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        try:
            cleaned_filename = filename.split(".")[0] + ".csv"
            subprocess.run(f"PresentMon-1.7.0-x64.exe -etl_file {os.path.join(etw_folder, filename)} -output_file {os.path.join(converted_folder, cleaned_filename)} ")
        except:
            print("errored")

if __name__ == "__main__":
    etw_to_pmon()