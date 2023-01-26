Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "Zophie a cat"
>>> name = name[:5] + "the" + [8:]
SyntaxError: invalid syntax
>>> newName = name[:5] + "the" + [8:]
SyntaxError: invalid syntax
>>> newName = name[0:5] + "the" + [8:10]
SyntaxError: invalid syntax
>>> newName = name[1:5] + "the" + [8:10]
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> name = 'Zophia a cat'
>>> newName = name[0:5] + "the" + [8:10]
SyntaxError: invalid syntax
>>> newName = name[0:5] + 'the' + [8:10]
SyntaxError: invalid syntax
>>> newName = name[0:5]+' the '+[8:10]
SyntaxError: invalid syntax
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name = name[0:7] + 'the' + name[8:12]
>>> name
'Zophia the cat'
>>> print("I changed the immutable string, just remember immubtability isn't unchangeability"+name)
I changed the immutable string, just remember immubtability isn't unchangeabilityZophia the cat
>>> 
