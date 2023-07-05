#Ask user to input whether they would like to use the calculator or read the text file
option = input("Enter '1' to use the calculator or '2' to read all previous equations from the text file: ")
#Keep asking user until either option 1 or 2 is selected
while option != "1" and option != "2":
    option = input("Invalid Input. Enter '1' to use the calculator or '2' to read all previous equations from the text file: ")

if option == "1":
    while True:
        try:
            number1 = float(input("Enter a number: "))
            # Check if the input number is a float or integer
            if isinstance(number1, (float, int)):
                break  # Exit the loop if a valid number is inputted
        except ValueError:
            # Handle the case when the input is not a number
            print("Invalid input. Please enter a number: ")

    #Ask user to input operation
    operation = input("Enter the operation: ")
    while operation != "+" and operation != "-" and operation != "x" and operation != "*" and operation != "/":
        operation = input("Invalid Input. Please enter the operation ('+', '-', 'x/*', '/'): ")

    while True:
        try:
            number2 = float(input("Enter a number: "))
            # Check if the input number is a float or integer
            if isinstance(number2, (float, int)):
                break  # Exit the loop if a valid number is inputted
        except ValueError:
            # Handle the case when the input is not a number
            print("Invalid input. Please enter a number: ")

    #Computing the result using user inputs
    answer = 0
    if operation == "+":
        answer = (number1 + number2)
    elif operation == "-":
        answer = (number1 - number2)
    elif operation == "x" or operation == "*":
        answer = (number1 * number2)
    elif operation == "/":
        answer = (number1 / number2)

    # Print the equation and result to the console
    print(number1, " ", operation, " ", number2, " = ", answer)
    equation = "{} {} {} = {} ".format(number1, operation, number2, answer)

    # Write the equation and result to a text file
    with open("equation.txt", "w") as f:
        f.write(equation)

elif option == "2":
    while True:
        try:
            #Ask the user for the name of the text file containing equations
            filename = input("Enter the name of the file containing the equations (e.g. equation.txt): ")
            
            #Open the file and read the equations
            with open(filename, "r") as f:
                equations = f.readlines()

            #Print the equations to the console
            for equation in equations:
                print(equation.strip())

            #Exit the loop if the file was read successfully
            break

        except FileNotFoundError:
            # Handle the case when the file does not exist
            print("File not found. Please enter a valid file name.")
