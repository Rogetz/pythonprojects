# code for shuffling a list
import random # has the shuffle method for shuffling a list

testList = ["trial","test","test3","test5","test10","test11"]
print("Initial List\n"+",".join(testList))
shuffledList = random.shuffle(testList)
# so this shuffler actually acts changes the original test List
print("after shuffling\n"+",".join(testList))