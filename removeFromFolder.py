import os
from pathlib import Path
import time
import shutil

def organizeDirectory():
    directoryPath = 'D:/Photography/Albums/2016'
    for item in os.scandir():
        if item.is_dir():
            folder = Path(item)
            str(folder)
            for items in os.scandir(folder):
                items.rename(directoryPath)
                print(items)
        
        # fileDateRaw = os.path.getmtime(filePath)
        # fileDate = time.ctime(fileDateRaw)
        # year = fileDate[20:24]
        # month = fileDate[4:7]
        # day = fileDate[8:10]
        #month = filePath[5:7]
        # if month == "01" :
        #     month = "Jan"
        # if month == "02" :
        #     month = "Feb"
        # if month == "03" :
        #     month = "Mar"
        # if month == "04" :
        #     month = "Apr"
        # if month == "05" :
        #     month = "May"
        # if month == "06" :
        #     month = "Jun"
        # if month == "07" :
        #     month = "Jul"
        # if month == "08" :
        #     month = "Aug"
        # if month == "09" :
        #     month = "Sep"
        # if month == "10" :
        #     month = "Oct"
        # if month == "11" :
        #     month = "Nov"
        # if month == "12" :
        #     month = "Dec"
        # directory = year + " " + month + " " + day
        # directoryPath = Path(directory) # Creates a new pathway in the PC for the file movement
        # if directoryPath.is_dir() != True: # If the path doesn't have an actual directory
        #     directoryPath.mkdir() # Make a directory (a folder) that has the name of "directory" variable.
        # filePath.rename(directoryPath.joinpath(filePath)) # Takes the path of item and renames it to: the directory
        #                                                   # concatenated with the the file name.
        #                                                   # Ex. From /etc.jpg -> /newDirectory/etc.jpg
        # print(directory)

organizeDirectory()