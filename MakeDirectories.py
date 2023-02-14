# This file is meant to create directories that can be used to automatically create my files.
import os

# used to create a series of directories
# notice that it can create both single files and many files.
# And also note that if a file is already created it generates a file created error so ensure that its not already created.
# Also remenmber you shouldn't refer to the variable name since the second time you call it its already created and generates an error.
try :
    directoryCreated = os.makedirs(r"D:\MyPythonGeneratedDirectory\test\directoryOne")
except :
    print("File already exists")

try: 
    directoryCreated2 = os.makedirs(r"D:\MyPythonGeneratedDirectory\test2\directoryOne")
except :
    print("directory already created")


print("Try calling the D:\MyPythonGeneratedDirectory\test2\directoryOne  to see if it really exists")
try :
    singleDirectoryCreated = os.makedirs(r"D:\TestOneDirectory")
except:
    print("The directory already created")
print("The single directory created is : D:\MyPythonGeneratedDirectory\test2\directoryOne")


