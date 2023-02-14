import re

regexCompiler = re.compile(r"((\\|/)\w+)$")
searchedRegex = regexCompiler.search("fILES\SEARCHING")
print(searchedRegex.group(1))
pathVariable = "fILES\SEARCHING"
# try replacing it using the sub method.
newStringFormed = regexCompiler.sub(r"",pathVariable)
print(newStringFormed)


def fileReplacer(filePath) :
    regexCompiler = re.compile(r"((\\|/)\w+)$")
    newStringFormed = regexCompiler.sub(r"\\",filePath)# here it appends a forward slash after it has been traversed
    return newStringFormed

# testing the function
valueReturned = fileReplacer("files/Searching")
print(valueReturned)