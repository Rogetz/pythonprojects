
# Testing the try catch block to know how to smoothly handle exceptions.
print("Testing the try catch block to know how to smoothly handle exceptions.\n Take note that the try except block can not catch syntax erors,simply because the syntax errors prevent the try except block itself from even running, hahahahahaha. ")
try :
    print("this is a division error test")
    result = 5/0
    print(str(result))
except :
    print('\n\nexception found I handled it well though please')

#   Raising an error
value = 7
print("\n\nAm just raising an exception to see it halting the process hahaha")
if value < 8 :
    raise  Exception(' the value must be more than or equals to 8')

# IGNORING an exception.
print("Testing the try catch block to know how to smoothly handle exceptions.\n Take note that the try except block can not catch syntax erors,simply because the syntax errors prevent the try except block itself from even running, hahahahahaha. ")
try :
    print("this is a division error test")
    result = 5/0
    print(str(result))
except :
    pass # safest way to ignore an exception