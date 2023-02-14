# This is the file for identifying the absolute directory name of a file
import os


dirName = os.path.dirname(r"D:\")
absolutePath = os.path.abspath(r".")

print("The dir name is: \n"+dirName+"\n")
print("The absolute path is: \n"+absolutePath+"\n")