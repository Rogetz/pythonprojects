import pyperclip

# this programm is a great one, you can use it for copying from sites and quickly appending to the grouo of text some symbols or other words as a whole.
clipText = pyperclip.paste()# pasting from the clipboard

clipTextArray = clipText.split("\n") # note that the markup should add stars for every single separate line

# NOTE THAT I am using the in range style an not in arrayItems style because here we are modifying the contents of the array and during modificatu=ion you need the reference to the variable not just the variable.
for i in range(len(clipTextArray)) :
    clipTextArray[i] = "*"+clipTextArray[i]

# convert the array back to the string it was.
convertedString = "\n".join(clipTextArray)
pyperclip.copy(convertedString)# copy it to the clipboard