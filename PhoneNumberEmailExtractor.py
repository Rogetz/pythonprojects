# This extracts from the clipboard.then returns a formatted one.
# worked perfectly fine.
import re
import pyperclip

regexCompiler = re.compile(r"(01|07|\+\d{3})(\d{8})|(\w+)(\d?)(@)(w+)(\.)(com)")
pyperclipCopied = pyperclip.paste()
returnedRegex = regexCompiler.search(pyperclipCopied)# the returned Regex

# findall works with groups so basically anything that is not in the brackets is never returned.
actualResult = regexCompiler.findall(pyperclipCopied)# findall uses the regex compiler directly and not the searched one like the group method
# fortunately you have to convert the list returned to string first before copying them back
newResult = "The Phone numbers and emails extracted are:-\n"
for i in actualResult :
    emailRegexCompiler = re.compile(r"(\w+\d*)(@)(w+)(\.com)")
    emailRegexSearcher = emailRegexCompiler.search("".join(list(i)))# had to convert the tuple to list and back to string for it to work.
    """if emailRegexSearcher != None:
        newResult += "~"+"".join(list(i))+"\n"
    else :"""
    # convert to list first then to string before joining, since find all has returned a list of tuples do to the number of groups it has.
    newResult += "*"+" ".join(list(i))+"\n"



#stringifiedResult = "\n".join(actualResult)

pyperclip.copy(newResult)


