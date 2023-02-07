#this file goes through a directory recursively and copies all the csvs to a single directory

import shutil
import glob
import os
from pathlib import Path

def recursive_copy():
    for path in Path(os.path.join("StutterData", "Copied")).rglob('*.csv'):
        # print(path)
        shutil.copy(path, os.path.join("StutterData", "all_copied"))

if __name__ == "__main__":
    recursive_copy()

