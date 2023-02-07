This folder is for the creation of scripts and tools for stutter detection.

Below is a short summary. For a much more detailed explanation of the project, check out the Confluence within these links:

Github link - https://github.amd.com/GPU-Solutions/bloodhound_soln/tree/master/infrastructure/Stutter_Detection
Network share - \\amd.com\tor\sse_solutions\Bloodhound\Stutter_detection
Confluence Page - https://confluence.amd.com/display/SSET/Machine+Learning+Stutter+Detection

Many of the files are one-time pre-reqs or useful tools not crucial to the future operation of stutter detection.

Key files include:
preprocessing.py, preprocessing_functions.py, main.py, predict.py

As well, the majority of the training data is not included in the git repository. One can find
this in the network share. 

To run locally, 
- Run pip install -r requirements.txt to install the proper dependencies.
- The workflow is as follows:
    - organize the correct directories
    - preprocessing of the data in preprocessing.py. preprocessing_functions.py contains all these functions and is also tested in test_preprocessing_functions.
    - this will create .ob files from pickle. We upload this Google Colab link here:
    - we can then download the .h5 model from there
    - then we use optimizing_local.py to test the model stats
    - finally, in main.py, it can be used on real systems


Current Directory
StutterDetection
- Models (contains the .h5)
- Old/Other
- Pickles (contains the .ob and scaler)
- Results (contains preliminary results on the data and model statistics including visuals)
- StutterData (contains stutter and nonstutter data)
rest of python files

On a test system:
- need: main.py, predict.py, preprocessing_functions.py, PresentMon, model10current.h5, scaler.ob, requirements.txt(pip install -r requirements.txt), 