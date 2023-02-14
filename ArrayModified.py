

for i in range(4):
    print("ABCD"[i])

#worked perfectly fine.
for i in range(4):
    # actually I realized that this method converts the string to an  array
    # meaning that this style works perfectly fine with an array.
    print("(%s).%s"%("ABCD"[i],"chapatiMoto"))

def choiceCreator(array):
    print("\n\n")
    for i in range(len(array)):
        print("(%s).%s"%(array[i],"chapatiMoto"))

choiceCreator(["A","B","C","D"])
choiceCreator(["a","b","c","d","e","f"])