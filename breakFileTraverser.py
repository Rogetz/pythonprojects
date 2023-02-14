# This is the file traverser meant to search for a file in the most fastest and shortest way possible
# afterwards maybe if you need the file to be opened you can tell it to
import os # never forget to import the os module for these tasks.
# emerging problem, the except block isn't displaying what I want it to display


driveD = "D:\\"
filename = "animations.pdf"

# Rememer that a function is defined with the def keyword and not tthe "define" keyword.
def fileTraverser(driveToTraverse,fileToLookFor) :

    if(os.path.isdir(driveToTraverse)): # assert first of all that it is a directory before jumping on to a NotADirectoryError
        try :# try catch block should always be called in such a way that it doesn't affect whatever loop has been set up.
            filesInTheDirectory = os.listdir(driveToTraverse)
            for directory in  filesInTheDirectory:
                if os.path.exists(os.path.join(driveToTraverse,fileToLookFor)) :
                    raise Exception("File exists Exception")
                    # I want it to exit from the function the moment it gets the file's path. do am using an exception that I will catch
                driveDerivedforTraversing = os.path.join(driveToTraverse,directory)# creating some new absolute paths
                fileTraverser(driveDerivedforTraversing,fileToLookFor)
        except :
            pass
            #pass is the safest way to ignore an exception block   
         
try:
    fileTraverser(driveD,filename)
except :
    print("The file"+fileToLookFor+"has been found in : \n"+os.path.join(driveToTraverse,fileToLookFor))


    