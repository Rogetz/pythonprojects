import os

driveD = "D:\\"

for directory in os.listdir(driveD):
    print(os.path.abspath(directory)) # This absolute path does not return the absolute path of what is passed in to it. Intead it uses is folder its called on as its arent directory.

print('\nThis is the final dirnam function for deriving the dirctory names.')
for directory in os.listdir(driveD) :
    print(os.path.join(driveD,directory))