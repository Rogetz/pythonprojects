# This file is meant to check when an operation began and when it ended as well as giving the correct actual time when it started and when it ended.
import time,re


def timeExtractor(unformattedTime) :
    regexCompiler = re.compile(r"(\d{2}:\d{2}:\d{2})")
    searchedCompiler = regexCompiler.search(unformattedTime)
    group = searchedCompiler.group(1)

    return group

startTime = time.ctime()
print("\nstart time:- "+timeExtractor(startTime)+"\n\n")
timeInEspoch = time.time()
print(timeInEspoch)
timeInCurrentTime = time.ctime(timeInEspoch)# brings the same result as one without a parameter.
print(timeInCurrentTime)
cTimeTest = time.ctime()# this has not been passed any parameter btw.
print(cTimeTest)
print("Trying to test whether I can filter the hours and minutes separatelyand it worked, wooow am happy and grateful, Its GOD")
#timeNow = cTimeTest.strftime("%H:%M:%S")# this strftime was from the web and it actually didn't work
endTime = time.ctime()
print("\nEnd time :- "+timeExtractor(endTime)+"\n\n")
print("The time taken to complete the file is null: I'll try find a way to isolte parts of the time so that they can be used in appropriate subtraction of time in seconds.")

