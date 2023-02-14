initialDictionary = {}# this is the initial dictionary that I have created.

# One trick of the dictionary is to ensure that all the values corresponding to the kwys are of different types so that
# you can easily iterate over all teh values of a key.
# for example in this case this dictionary has string type of keys and list type of values
initialDictionary["firstRecord"] = [700]
initialDictionary["secondRecord"] = [250,350,150]
initialDictionary["secondRecord"].append(265)
# at the same time we can use the concatenation symbol + to concatenate it with another array.
# example
initialDictionary["secondRecord"] += [255]# I have concatenated another array with this to form a new array.

# This is the dictionaryPrinter method that is meant to print each values of a key
def dictionaryPrinter(dictionary) :
    for singleKey in dictionary.keys():
        print("These are the values of the key "+singleKey+" :")
        # note that whatever is returned by the keys() method is simply a name.
        stringArray = []
        for singleInteger in dictionary[singleKey] :
            stringArray.append(str(singleInteger))
        
        print("\n".join(stringArray)+"\n")# do note that the join doesn't work well with any other type array so I've had to convert each type to string first individually before appending it to a string array that I have created.

dictionaryPrinter(initialDictionary)