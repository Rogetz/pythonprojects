# import two or more once
import pyperclip,re

#regexCompiler = re.compile(r"(\w+)(\d?)(@)(w+)(\.)(com)") # this was my own created regex.
pyperclipCopied = pyperclip.paste()
regexCompiler = re.compile(r'''(
u [a-zA-Z0-9._%+-]+ # username
v @ # @ symbol
w [a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)# this was a copied regex from the book. Still it didn't function.

# findall works with groups so basically anything that is not in the brackets is never returned.
actualResult = regexCompiler.findall(pyperclipCopied)

newResult = "The Phone numbers and emails extracted are:-\n"
for i in actualResult :
    """emailRegexCompiler = re.compile(r"(\w+\d*)(@)(w+)(\.com)")
    emailRegexSearcher = emailRegexCompiler.search("".join(list(i)))# had to convert the tuple to list and back to string for it to work.
    """
    """if emailRegexSearcher != None:
        newResult += "~"+"".join(list(i))+"\n"
    else :"""
    # convert to list first then to string before joining, since find all has returned a list of tuples do to the number of groups it has.
    newResult += "*"+"".join(list(i))+"\n"


pyperclip.copy(newResult)