import re

# I have now really understood groups, they are simply any form of regex enclosed in brackets.inclusing a word
# so the thing here is that even if a certain letter is part of a regex but its  not in brackets its not counted as a group.
# Regex groups start counting from where there's a bracket.

regexCompiler = re.compile(r'Agent (\w)\w+')
searchedRegex = regexCompiler.search("Agent Alice gave the secret documents to Agent Bob")
print(searchedRegex.group(1)+"rem: its only matching the single A because of how its a single keyword without any regex modifier")
# so after a keen investigation I've just realized that the numbers that I pass on to the sub method are just but symbols themselves
# for example a 1 stands for a smiley while a 5 stands for an arrow symbol.
# This preceding observation was just a joke. The actual verified one is here below.
# I realized that if the interpreter doesn't understand the values passed to it gives it a smiley and thats what had actually happened earlier on.
result = regexCompiler.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.')
wordyString = 'Agent Alice gave the secret documents to Agent Bob.'
result2 = regexCompiler.sub(r'\1***',wordyString)
print(result2)
print("surprisingly the regex replacement isn't permanent:-")
print(wordyString+"\n\n")
print("This below is just printing the regex returned, so basically the regex doesn't modify the original value, it creates a new one which is still a good thing since you can work with it")
print(result)


# This one is one for ignoring the casing in the regex.
print("\nOne regex ignoring the casing in the string")
regexCompiler2 = re.compile(r'AGENT (\w)\w+',re.IGNORECASE)# pass the re.VERBOSE while creating the regex compiler, for it to ignore all manner of cassings later on during the search.
searchedRegex2 = regexCompiler2.search("agent alice gave the secret documents to agent Bob")
print(searchedRegex2.group(1))

# This one is one for ignoring the white spaces in the regex I dont know where I'll use it later but lemme just preserve it for later use.
print("\nOne regex ignoring the whites spaces including the newlines and the spacing in the string")
regexCompiler3 = re.compile(r'Agent (\w)\w+',re.VERBOSE)# pass the re.VERBOSE while creating the regex compiler, for it to ignore all manner of cassings later on during the search.
searchedRegex3 = regexCompiler3.search("AgentAlice gave the secret documents to Agent Bob")
# The regex is one very cool thing btw.
print(searchedRegex3.group(1))
print(regexCompiler3.findall())# uses the regex compiler direcly
