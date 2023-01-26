Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'Hello World!
SyntaxError: EOL while scanning string literal
>>> 'Hello World!'
'Hello World!'
>>> "Paul" * 5
'PaulPaulPaulPaulPaul'
>>> "Paul  " *5
'Paul  Paul  Paul  Paul  Paul  '
\
>>> Spam = "Hello There"
>>> spam
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> Spam
'Hello There'
>>> Spam = "Goodbye Guys"
>>> Spam
'Goodbye Guys'
>>> print("I am 22 years Old")
I am 22 years Old
>>> Age = 22
>>> print("I am"+str(Age)+"Years Old")
I am22Years Old
>>> print("I am"+str(Age)+"Years Old")
I am22Years Old
>>> print("I am "+str(Age)+" Years old")
I am 22 Years old
>>> rawInput = input()
22
>>> print(rawInput)
22
>>> there are seven rivers in Africa Nile, niger Senegal, Congo, Orange Limpopo nA ZAMBEZI
SyntaxError: invalid syntax
>>> castInt = int(rawInput)
>>> addition = castInt + 7
>>> print(addition)
29
>>> # by default python takes every input as an integer which is pretty much the same  thing in all the other languages.
>>> # For finding the length of strings please use the len() function
>>> # e.g
>>> testString = 'I am a child of GOD'
>>> print("The length of the testString is"+str(len(testString)))
The length of the testString is19
>>> print("The length of the testString is  :"+str(len(testString)))
The length of the testString is  :19
>>> #In python the boolean operators are in words and not in symbols as in the ccase of all the other languages whereby they are categorized as logical operators.
>>> (5+5) and (10+10)
20
>>> (5+5) and (10+10) == (10+15)
False
>>> # boolean operators are used mostly in If statements and  in  the comparison of large strings of text.

>>> # In python the for loop is used with the in range() method and not the normal for loop we are used to in the other languages.
>>> for i in range(5):
	print("I'll count how many times its printed")

I'll count how many times its printed
I'll count how many times its printed
I'll count how many times its printed
I'll count how many times its printed
I'll count how many times its printed
>>> # in the in range function is placed at the end as opposed to the normal lop  where its place at the start.
>>> for i in  range(1,50,2):
	print('feels goos setting a step value for the in range function")
	      
SyntaxError: EOL while scanning string literal
>>> for i in  range(1,50,2):
	print("feels goos setting a step value for the in range function")

feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
feels goos setting a step value for the in range function
>>> # You can as well reverse the chain bruh
	      
>>> for in range(5,-1,2):
	      
SyntaxError: invalid syntax
>>> for i in range(5,-1,2):
	      print("I have reversed the loop")

>>> for i in range(5,-1,-2):
	      print("I have reversed the loop")

I have reversed the loop
I have reversed the loop
I have reversed the loop
>>> # also note that while reversing you also negate the step value.

>>> # modules in python are imported using the import keyword.
	      
>>> import random
	      
>>> print("A random number between 1 and 5 :- "+random.randint(1,10))
	      
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print("A random number between 1 and 5 :- "+random.randint(1,10))
TypeError: can only concatenate str (not "int") to str
>>> print("A random number between 1 and 5 :- "+str(random.randint(1,10)))
	      
A random number between 1 and 5 :- 1
>>> print("A random number between 1 and 5 :- "+str(random.randint(1,10)))
	      
A random number between 1 and 5 :- 8
>>> for i in range(1,5):
	      print(' A random number between 1 and 10"+str(random.randint(1,10)))
		    
SyntaxError: EOL while scanning string literal
>>> for i in range(1,5):
	      print(' A random number between 1 and 10 '+str(random.randint(1,10)))

 A random number between 1 and 10 5
 A random number between 1 and 10 1
 A random number between 1 and 10 2
 A random number between 1 and 10 6
>>> # using functions from imports directly, and actually  this is the style that I willl borrow
		    
>>> from random import *
		    
>>> print("A random number between 1 and 5 :- "+str(randint(1,10)))
		    
A random number between 1 and 5 :- 3
>>> # worked perfectly fine
		    
>>> # testing the sys module, specifically the exit() method in it
		    
>>> from sys import *
		    
>>> initialValue = 1
		    
>>> while initialValue == 1:
		    name = input("Enter Name or type exit to exit")
		    if name == "exit":
			exit()
		    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while initialValue == 1:
		    name = input("Enter Name or type exit to exit")
		    if name == "exit":
					exit()
		    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while initialValue == 1:
		    name = input("Enter Name or type exit to exit")
		    if name == "exit" :
		    exit()
		    
SyntaxError: expected an indented block
>>> while initialValue == 1:
		    name = input("Enter Name or type exit to exit")
		    if name == "exit" :
				    exit()
		    elif name == "Ronny" :
				    print("Hello sir")
		    else :
				    print("Your name is: "name)
		    
SyntaxError: invalid syntax
>>> while initialValue == 1:
		    name = input("Enter Name or type exit to exit")
		    if name == "exit" :
				    exit()
		    elif name == "Ronny" :
				    print("Hello sir")
		    else :
				    print("Your name is: "+name)

Enter Name or type exit to exitTom
Your name is: Tom
Enter Name or type exit to exitPaul
Your name is: Paul
Enter Name or type exit to exitRonny
Hello sir
Enter Name or type exit to exitRonny
Hello sir
Enter Name or type exit to exitexi
Your name is: exi
Enter Name or type exit to exitexit
>>> while initialValue == 1:
		    name = input("Enter a Name or type exit to exit:    ")
		    if name == "exit" :
				    exit()
		    elif name == "Ronny" :
				    print("Hello sir")
		    else :
				    print("Your name is: "+name)

Enter a Name or type exit to exit:    Tom
Your name is: Tom
Enter a Name or type exit to exit:    Paul
Your name is: Paul
Enter a Name or type exit to exit:    John
Your name is: John
Enter a Name or type exit to exit:    Ronny
Hello sir
Enter a Name or type exit to exit:    Ronny
Hello sir
Enter a Name or type exit to exit:    exit
>>> 
