dic1 = {'rope': 1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

# code for displaying the total no of items(which are in the values of the dictionary of course.) of the inventory.
def dispLayInventory(inventory) :
    print("Inventory: ")
    totalItems = 0;
    for k,v in dic1.items() :
        print(str(v)+" "+k)
        totalItems += v
    print("Total Number of items:  "+str(totalItems))    



dragonLooot = ['gold coin','dagger','gold coin','gold coin','ruby']
def addToInventory(inventory,addedItems) :
    for i in addedItems :
        if i in inventory.keys() :
            inventory[i] += 1
    
addToInventory(dic1,dragonLooot)
dispLayInventory(dic1)

print()
print("-----My own modified version of gold loot and addToInventory method-----")
# this is a modified version of the addToInventory which allows addition of items that were'nt there.
dragonLooot = ['gold coin','dagger','gold coin','gold coin','ruby','chapati','mandazi','Githeri','chapati']
def addToInventory(inventory,addedItems) :
    for i in addedItems :
        if i in inventory.keys() :
            inventory[i] += 1
        else :
            inventory[i] = 1;

addToInventory(dic1,dragonLooot)
dispLayInventory(dic1)
  