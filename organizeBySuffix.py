import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO" : ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "APPLICATION": ['.exe'],
    "ZIP": ['.zip']
}

def pickDirectory(value):
    for category,suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC' # If the file type doesn't match one of the SUBDIRECTORIES catergories then 
                       # it will return 'MISC' to make a MISC folder

print(pickDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir(): # Loops through the current directory and scans every item
        if item.is_dir(): # Checks if the item is already a directory
            continue # goes to next iteration of the loop
        filePath = Path(item) # Sets a variable that is assigned location path ex. /examples
        fileType = filePath.suffix.lower() # Variable that holds string data of the file type ex. ".jpeg"
        directory = pickDirectory(fileType) # Variable that returns name of directories that file should be placed into.
        directoryPath = Path(directory) # Creates a new pathway in the PC for the file movement
        if directoryPath.is_dir() != True: # If the path doesn't have an actual directory
            directoryPath.mkdir() # Make a directory (a folder) that has the name of "directory" variable.
        filePath.rename(directoryPath.joinpath(filePath)) # Takes the path of item and renames it to: the directory
                                                          # concatenated with the the file name.
                                                          # Ex. From /etc.jpg -> /newDirectory/etc.jpg
        
organizeDirectory()