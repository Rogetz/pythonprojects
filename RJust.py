

testString = "This is the string"
# The just methods and the center method, need a paramter specifying the scope that it
# will be working upon.
print(testString.ljust(len(testString)+5))
print(testString.rjust(len(testString)+5))
print(testString.center(len(testString)+5))

print(testString.ljust(len(testString)+5,"*"))
print(testString.rjust(len(testString)+5,"*"))
print(testString.center(len(testString)+5,"*"))

