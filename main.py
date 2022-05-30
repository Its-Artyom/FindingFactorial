###
# Algorithm that fins a factorial of a number
# Made by @its-artyom
###

# Input
try:
    number = int(input("Input a number you want to find the factorial of: "))
    factorial = 1 # Setting the starting value for the for-loop

    if number < 0:
        print("There are no factorials for negative numbers.")
    elif number == 0:
        print("The factorial of 0 is equal to 1")
    else:
        # For-loop that goes through every number from the input
        for _number in range(1, number + 1):
            factorial *= _number
            print(factorial)
        print("The factorial of " + str(number) + " is " + str(factorial))

except ValueError:
    print("Wrong type of value has been inputted, please input an integer.")