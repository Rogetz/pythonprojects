

def collatz(number):
    if number % 2 == 0 :
        number = number / 2
        print("number equals"+str(number))
        return number
    elif number % 2 == 1 :
        number = 3 * number + 1
        print("number equals"+str(number))
        return number
    else :
        print(str(number))
        return number

while True :
    try:
        # remember to cast it into an integer.
        inputNo = int(input("Input a number please "))
    except ValueError :
        print("Enter a number please next time")
        # using continue so that it doesn't evaluate with a wrong input.
        continue
    while inputNo != 1 :
        # python is very funny here, assigning a method does the calling as well as the assigning so I dont need to assign once more.
        inputNo = collatz(inputNo)
    print("final number equals" + str(inputNo))
    break
