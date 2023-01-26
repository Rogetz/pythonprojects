# In python a list is the equivalent of arrays and lists in other languages.
# Its very rich btw.

def commaCode(listOfItems):
    # initialize the string with null
    finalString = ""
    for i in listOfItems:
        if i != listOfItems[-1] and i != listOfItems[-2]:
            finalString +=  i+","
        elif i == listOfItems[-2]:
            finalString += i +" and "
        elif i == listOfItems[-1]:
            finalString += i
    print(finalString)

commaCode(["Tom","jERRRY"," goodluck","Peter"])

