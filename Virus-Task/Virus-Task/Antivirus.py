import os
#Get the current directory
cwd = os.getcwd()

virus_file =    "virusFile.txt"

with open(virus_file) as f:
        virus_text = f.read()
        f.close()

#Define the anti-virus function
def antivirus():
    #Get the list of files in the current directory:
    files = os.listdir(cwd)
    
    #Loop through the files 
    for file in files:
        with open(file) as f:
            contents  = f.read()
            if virus_text in contents:
                f.close()
                os.remove(file)
                print("infected file removed:", file)

#Call the anti-virus function
antivirus()