import os
from pathlib import Path
import time

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileDateRaw = os.path.getmtime(filePath)
        fileDate = time.ctime(fileDateRaw)
        year = fileDate[20:24]
        month = fileDate[4:7]
        day = fileDate[8:10]
        directory = year + " " + month + " " + day
        directoryPath = Path(directory) # Creates a new pathway in the PC for the file movement
        if directoryPath.is_dir() != True: # If the path doesn't have an actual directory
            directoryPath.mkdir() # Make a directory (a folder) that has the name of "directory" variable.
        filePath.rename(directoryPath.joinpath(filePath)) # Takes the path of item and renames it to: the directory
                                                          # concatenated with the the file name.
                                                          # Ex. From /etc.jpg -> /newDirectory/etc.jpg
        print(directory)
organizeDirectory()