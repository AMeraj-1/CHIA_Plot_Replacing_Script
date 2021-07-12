# Author: AMeraj
# File Modified: 12/07/2021
# Version: 0.0.1

import os
import sys
import time
import glob
from os import listdir

# Maximum exisiting file to replace/remove
File_Count = 3;
print("Max Plots to remove: " + str(File_Count))

# Plot Temp Directory - MadMax Temp Folder
Temp = r"C:/Users/xxxx/Desktop/Plot_Create/"
print("Temp Directory: " + Temp)

# Solo Plot Destination Directory
Destination = r"C:/Users/xxxx/Desktop/Plot_Destination/"
print("Final Directory: " + Destination)

# Plot Extention
extention = ".plot"

# Function to remove old files
def Remove_Old_File():
    global File_Count
    # List files in directory
    Directory_List = os.listdir(Destination)
    Plot_Loc = Directory_List[0]

    # If file exisit remove file
    if any(File.endswith(extention) for File in os.listdir(Temp)):
       os.remove(os.path.join(Destination, Plot_Loc))
       print("Plot Removed : " + Plot_Loc)
       File_Count = File_Count - 1
       print("Wait Copying") 
       time.sleep(1800)
       print("Process Resumed") 
    else:
        print("No New Plot Detected")


# Looping
while File_Count > 0:
    print("Checking Plots every 5 min - Plot remaining: " + str(File_Count))
    Remove_Old_File()
    time.sleep(300) 





    


