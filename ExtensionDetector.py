import re

def extensionDetector(fileToCheck):
    regexCompiler = re.compile(r"(\.\w+)$") # note that you must escapes special characters in regex
    # such as \ . since they have very special meanings in regex, so even if you use the raw dtring, you still have to escape them
    searchedCompiler = regexCompiler.search(fileToCheck)
    group = searchedCompiler.group(1)
    return group


print(extensionDetector(r"D:\directoryHolder\testing\animations.pdf"))