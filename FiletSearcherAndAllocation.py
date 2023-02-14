# This is the file meant to traverse all the files in the computer system and categorize them into files depending on their file extensions.
import os,re,sys # never forget to import the os module for these tasks.

# Do note that the try catch block here runs very smoothly when you run it in the Win + R GUI
# funny thing here you use the py.exe which actually I think is the actual good executor more than the python
# ensure that you pass the absolute path of the file  to the py.exe



def extensionDetector(fileToCheck):
    regexCompiler = re.compile(r"(\.\w+)$")
    searchedCompiler = regexCompiler.search(fileToCheck)
    group = searchedCompiler.group(1)
    return group

def fileReplacer(filePath) :
    regexCompiler = re.compile(r"((\\|/)\w+)$")
    newStringFormed = regexCompiler.sub(r"\\",filePath)
    return newStringFormed


# An explanation of the recursive functions from stack overflow is that each function returns the value to its caller.
# Remember that a function is defined with the def keyword and not tthe "define" keyword.
def fileTraverser(driveToTraverse,fileToLookFor,extensionsStored) :
    print('entered the function')
    # Eliminated this since here I am only trying to look for files and not directories.
    # And it was actuallty the bug
    if os.path.isdir(driveToTraverse):
        print('entered the directory part') # assert first of all that it is a directory before jumping on to a NotADirectoryError
        #try :
        print("entered the try part")
        try :
            directoriesAndFilesInTheDirectory = os.listdir(driveToTraverse)
        except :
            pass
        for directory in  directoriesAndFilesInTheDirectory:
            # the bug was it wasn't reading the absolute path directory path name.
            try:
                absoluteDirPath = os.path.join(driveToTraverse,directory)

                print("entered directory  "+absoluteDirPath)
                if os.path.isfile(absoluteDirPath) :
                    print("entered a file")
                    print("\nfile  "+absoluteDirPath+"  found\n")
                    extensionFound = extensionDetector(absoluteDirPath)
                    # use the path.exists to test for existence instead
                    if extensionFound != "" and not os.path.exists(r"D:\FilesSearched\\"+extensionFound+"file"):
                        
                        # the extensionsStored list is not an array. I have removed it, I'll look for a way to persist it.
                        extensionsStored[extensionFound].append(directory)# the file should be appended ven if its the first time.
                        try:
                            os.makedirs(r"D:\FilesSearched\\"+extensionFound+"file") 
                            # I could instead just use open the file in write mode to create the file.
                            print("passed through the os.makedirs")
                            fileObject = open(r"D:\FilesSearched\\"+extensionFound+"file"+extensionFound+"file.txt","w")
                            fileObject.write("The files of "+extensionFound+"\n"+absoluteDirPath)
                            fileObject.close()# close it
                        except :
                            print("The file "+extensionFound+"file was already created")
                    # note that it only returns the names of the keys, and not the key vALUES themselves
                    if extensionFound != "" :# extensions stored is a dictionary
                        extensionsStored[extensionFound].append(directory)
                        fileObject = open(r"D:\FilesSearched\\"+extensionFound+"file"+extensionFound+"file.txt","a")
                        fileObject.write(","+absoluteDirPath)
                        fileObject.close()# close it
                        # I can as wel add the items one by one withou a dictionary
                        # look for a way to finally add all the dictionary after the whole process of recursion is full finished. 
                elif os.path.isdir(absoluteDirPath) :
                    # error is its not entering this os.path.is file and os.path.isdir part
                    print("entered a sub-folder  "+absoluteDirPath)
                    #print("extensionsStored is : "+str(extensionsStored))
                    #return extensionFound # Am trying to call it recursively to be returned to the majo caller.
                    fileTraverser(absoluteDirPath,fileToLookFor,extensionsStored)            
            except :
                pass
                
                """else :
                    driveDerivedforTraversing = os.path.join(driveToTraverse,directory)# creating some new absolute paths
                    fileTraverser(directory,fileToLookFor,extensionsStored)
                """
        """except :
            print("file/drive : "+driveToTraverse+"can not be accessed.It may due to permission errors")     
        """
    else :
        print("please input a valid directory "+driveToTraverse+" the programm must begin with an actual directory")
    
    """elif os.path.isfile(driveToTraverse):                    
        print("\nfile  "+driveToTraverse+"  found\n")
        extensionFound = extensionDetector(driveToTraverse)
        if extensionFound != "" and extensionFound not in extensionsStored :
            try:
                os.makedirs(r"D:\FilesSearched\ "+extensionFound+"file") 
            except :
                print('The file was already created')
        if extensionFound != "" :
            extensionsStored[extensionFound].append(directory)

        # uses the same path so it doesn't need any join method.
        # since this is a file so its still inside the same folder.
        drivegenerated = fileReplacer(driveToTraverse)# for it to remain in the same directory.
        # check on why it aint working
        print("drive generated here is: "+drivegenerated)
        fileTraverser(drivegenerated,fileToLookFor,extensionsStored)
    """



"""commented out, to sort tommorow.
def fileAllocator(drive,filechosen,extensionsUsed) :
    driveToStore = "D:\\FilesSearched\\"# Kept it like this bearing in mind that this is only a string.

    # look for a way to return a value/ the dictionary from the recursive function. and call it dictExtracted
    dictExtracted = fileTraverser(drive,filechosen,extensionsUsed)

    # I have defined the extension detector once again
    def extensionDetector(fileToCheck):
        regexCompiler = re.compile(r"(\.\w+)")
        searchedCompiler = regexCompiler.search(fileToCheck)
        group = searchedCompiler.group(1)
        return group

    for extractedKey in dictExtracted.keys() :
        file = open(driveToStore+extractedKey+"file","w")
        file.write(dictExtracted[extractedKey])# immediately append all the values of a specific key.
        file.close()
"""

# The one thing Hateful about python is its synchronous nature, It doesn't hoist the variables and functions. 
if len(sys.argv) == 3:
    driveD = sys.argv[1]
    extensionsStored = {}# This is the dictionary that the extension must work on and store the values and keys of the files
    filename = sys.argv[2]
    # try catch block should always be called in such a way that it doesn't affect whatever loop has been set up.
    fileTraverser(driveD,filename,extensionsStored)
else :
    print("please fill out the two arguments, drive name and the filename to be used in the search")
