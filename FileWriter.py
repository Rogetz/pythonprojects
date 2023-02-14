import os # its not needed by the open method but I have just kept in for just in case

# for appending data without overrwriting
# seems like the open is an inbuilt method in python.
fileObj = open("test.txt","a") # append mode
fileObj.write("\nThis is another appended text")
fileObj.close()# always close after using it.

# for overwriting and creating a file
fileObj2 = open("test2.txt","w")# write mode
fileObj2.write("\nThis is the first text, and the file was automatically created by the open method.")
fileObj2.close() # closing

# for reading the file.
# if you hadn't closed the file previously, it will generate an error.
fileObj3 = open("test2.txt","r")# read mode
readResult = fileObj3.read()
fileObj3.close()# closing
print("\n"+readResult)