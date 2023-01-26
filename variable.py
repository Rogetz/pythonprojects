numberArray = [14,25,35]
stringTest = "this is the string"

print("/*----This is the variable test in python------*/")

# One great feature of python inputs is that you can easily write data to the input directly to be displayed as a helper as to what is really needed.
inputRead = input("Input some data to be read   Please---: ")

#note that casting in python is done a bit different, its somehow using a str as a method  to cast instead of using the normal cast as in the case of c# and most programming languages.
print("This is the input read: "+str(inputRead))
print("This is the numberArray cast to a string: "+str(numberArray))
print("This is the stingTest so no need to cast it to an array  "+stringTest)