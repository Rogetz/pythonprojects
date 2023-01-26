import copy
# the copy module must first be imported.

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

newGrid = copy.deepcopy(grid)

# newer syntax printing as required.
indexing = 0;
while True:
    for gridNo  in range(len(newGrid)):
        # see the main issue was that its comparing with the values and not the index, but it should actually be using the index
        # cause if its a matter of values then the last index might be  the same with the first.
        if gridNo == (len(newGrid) - 1):
            print()
        print(newGrid[gridNo][indexing],end="")
    indexing += 1;
    if indexing == (len(newGrid[0])) :
        break;
print("---------End------------")
print("This is the previously disturbing code, I've made it work, Though this was not what the challenge wanted")
print("And the parameters passed to the end literal work perfectly fine with no issues.")
newString = ""
count = 0;
typeHolder = "";
for i in newGrid:
    for littleINo in range(len(i)):
        if littleINo == (len(i) - 1):
            print(i[littleINo],end="\n")
        elif littleINo != (len(i) - 1) :
            print(i[littleINo],end='')
        count += 1;
        typeHolder = str(type(i))
        
            
print(str(count));
# this is just to show that it can as well print integers directly.
print(count)  
