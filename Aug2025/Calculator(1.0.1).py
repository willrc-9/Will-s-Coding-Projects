#Functions used!!

# function that ensures your input is a number
def getNum(prompt):
    while True:
        num = input(prompt)

        # try to make an int first
        try:
            num = int(num)
            return num
        except ValueError:
            pass
        
        # next tries float if int did not work
        try:
            num = float(num)
            return num
        except ValueError:
            print("Not an acceptable value. Please Try again.")


# determines if number is whole or not
# just something to make the number prettier on the final result
# so instead of printing ex. 5.0, it prints 5

def checkIfWhole(num):
    return num == int(num)

print("Welcome! Will you be (a)dding, (s)ubtracting, (m)ultiplying, or (d)ividing?")

while True:
    # a loop that ensures the user actually inputs a proper respsonse
    while  True:

        device = input("Please input the letter associated with the math function you desire, or 'q' to quit (No caps please!): ")

        if device == "q":
            print("Understandable. Have a great day!")
            break
        elif device != "a" and device != "s" and device != "m" and device != "d" and device != "q":      
            print(device + " is not an acceptable response.")
            continue
        else:
            if device == "a":
                devicen = "+"
                devicena = "add"
                print("You chose addition!")
            elif device == "s":
                devicen = "-"
                devicena = "subtract"
                print("You chose subtraction!")
            elif device == "m":
                devicen = "x"
                devicena = "multiply"
                print("You chose multiplication!")
            else:
                devicen = "/"
                devicena = "divide"
                print("You chose division!")
            break

    # gathers inputs
    while True:
        num1 = getNum("Please input the first number which you would like to " + devicena + ": ")
        num2 = getNum("Please input the next number which you would like to " + devicena + ": ")
        break

    # the actual math here
    if devicen == "+":
        result = num1+num2
    elif devicen == "-":
        result = num1-num2
    elif devicen == "x":
        result = num1*num2
    else:
        result = num1/num2

    # doing the other stuff to make the number pretty if whole
    if checkIfWhole(result):
        result = int(result)

    # printing result!
    print(str(num1) + " " + str(devicen) + " " + str(num2) + " = " + str(result))

    # asking if you would like to continue, and restarting loop if yes. thanking you and ending if not
    while True:
        cont = input("Would you like to continue? y/n: ")
        
        if cont.lower() in ["y", "n"]:
            break
        else:
            print("Not a valid response.")
            continue
    if cont.lower() == "y":
        continue
    else:
        print("Thank you for using my calculator!!!")
        break

