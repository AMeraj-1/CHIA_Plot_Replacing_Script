# CHIA_Plot_Replacing_Script

This scripts can be used to run along MadMax plotter to remove old solo plot when new NFT plot is finished by MadMax

**Pre-requisite **
---------------------------------------------------------------------------------------------------------------
Python 3.5

**Script Overview**
---------------------------------------------------------------------------------------------------------------
The idea here is to create a new folder for new NFT plots in the same drive where you want to remove old solo plots.
The script scans the MadMax temp folder every 5 mins (can be modified according to user need) and if the new plot is 
found then script will remove 1 old solo plot and then wait for the copy to be finished before resuming the process. 
This script doesn't copy the plot itself however it waits 30 mins (can be modified according to user need) before resuming
the process. To modify the script please right click and use edit with idle option to modify the script.

**Script using guide**
---------------------------------------------------------------------------------------------------------------
Step-1: Create new empty folder in the solo plot directory

Step-2: Copy the address to script "Destination" variable 

![image](https://user-images.githubusercontent.com/87322367/125312116-e9c47f80-e32b-11eb-8d06-f816a584e1ea.png)

Step-3: Copy the temp drive location to script where MadMax is going to finish plotting

![image](https://user-images.githubusercontent.com/87322367/125312251-05c82100-e32c-11eb-9d8f-3170293ae4f8.png)

Step-4: set the number of plots you want to remove by this script.

![image](https://user-images.githubusercontent.com/87322367/125312382-209a9580-e32c-11eb-9172-069e3b63ee9e.png)

Step-5: Close the script and run the file by double clicking
