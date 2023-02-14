import os # module for testing for existence of any file  or directory, the fastest I have seen

# do not that I went deep into the user directory to see how fast this evaluate
# The speed amazed me Mahn.
# Result is a boolean by the way.
existenceResult = os.path.exists(r"D:\user\my_folder\my tings\programming books")#note how I have used the r flag to make it display it as raw strings and enable smooth reaing of the path.
print("The paths existence is : \n"+str(existenceResult))
