import pyperclip
import sys
# I ran this programm with a batch file called python-batch in my batchfiles folder and realized that you need to first pause the batch file inorder for you to see it executing and not for it to fade once called out by the Win R 
# Win + R is pretty much the same as working directly on the command line so you can direcly pass the command line arguments as if you were in the command prompt

"""pyperclip.copy("This is my text")
print(len(sys.argv))"""
passwords = {"Tony": "BestShebange",
"rufus25@gmail.com" : "TH51SGHBJS"
}

# sys.argv is the input from the command line argument prompt.
if len(sys.argv) < 2 :
    print("The account argument must be supplied, try again next time\n")
else :
    accountName = sys.argv[1];
    if accountName in passwords : 
        pyperclip.copy(passwords[accountName])
        print("\nthe password for"+accountName+"copied to the clipboard\n")
    else :
        print("\nThe name "+accountName+" is not in the passwords available")