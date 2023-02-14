# This programm is meant to accept a list if lists and print it right justified in a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


def printTable(listOfLists) :
    printableString = ""# always contain a functions methods such that they are not treated as globals and for easy manipulation
    for i in tableData :
        printableString = printableString + " ".join(i)+" "
        # investigate for a method to find the largest value in a list of strings.
    convertedArray = printableString.split(" ")
    print(max(convertedArray,key=len))
    longestString = max(convertedArray,key=len)
    print(printableString)
    for i in listOfLists : 
        for j in range(len(i)) :
            print("|"+i[j].rjust(len(longestString)+4,"*"),end="")
            if j == (len(i) - 1):
                print("|"+"\n")
    for k in listOfLists : 
        for j in range(len(k)) :
            print("|"+k[j].ljust(len(longestString)+4,"*"),end="")
            if j == (len(k) - 1):
                print("|"+"\n")
    for l in listOfLists : 
        for j in range(len(l)) :
            print("|"+l[j].center(len(longestString)+4,"*"),end="")
            if j == (len(l) - 1):
                print("|"+"\n")

printTable(tableData)