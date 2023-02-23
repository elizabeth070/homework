print("Hello, user! Welcome to this Python calculator.\n")

valid_operations = ['1', '2', '3', '4']

#defining operations functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero\n")
    return num1 / num2

#main while loop
while True:
    print("Please choose the operation you would like to perform by typing its number.\n")
    print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n")
    operation = input()

    #error checking
    if operation not in valid_operations:
        print("The operation you have entered is invalid. Choose from 1 to 4\n")
        continue

    print("Enter your numbers as decimal values separated by a dot - e.g. 4.57\n")

    #accepting user input
    while True:
        num1_input = input("Enter your first number:\n")
        try:
            num1 = float(num1_input)
        except ValueError:
            print("Invalid input. Please enter a number\n")
            continue
        break

    while True:
        num2_input = input("Enter your second number:\n")
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input. Please enter a number\n")
            continue
        break

    #linking operations to functions
    if operation == '1':
        result = add(num1, num2)

    elif operation == '2':
        result = subtract(num1, num2)

    elif operation == '3':
        result = multiply(num1, num2)

    else:
        try:
            result = divide(num1, num2)
        except ZeroDivisionError:
                print("Cannot divide by zero!\n")
                continue

    #output
    print("Result: {:.2f}".format(result))
    
    #option for user to continue or exit out of the main loop
    while True:
        answer = input("Would you like to perform another operation? Type y / n:\n")

        if answer == 'n':
            print("Thank you for using this Python calculator!\n")
            break
        elif answer =='y':
            break
        else:
            print("Invalid response. Please type y or n\n")

    if answer == 'n':
        break
