#this file gets all the csvs (not etls) from a network share

import shutil
import os
from shutil import copytree, ignore_patterns

def grab_csvs():
    source = "\\\\orlsw\\analysis\\Stutter\\Top Tier Data"
    destination = "StutterData\\Copied"

    #avoids zip files and etls (very large files)
    copytree(source, destination, ignore=ignore_patterns('*.etl', '*.zip'))

if __name__ == "__main__":
    grab_csvs()
