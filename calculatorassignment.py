# A simple calculator python program that implements user input and output

# Function to perform calculations
def calculate(num1, num2, operation):

#This operation is addition
    if operation == '+':
        return num1 + num2
#This operation is subtraction
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
#This operation is multiplication
        return num1 * num2
#Thius operation is modulus
    elif operation == "%":
        return num1 % num2
##This operation is division
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Main program
print("Enjoy working with our Simple Calculator Program!")
try:
    # User inputs for numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, %): ")

    # Calculate and display the result
    result = calculate(num1, num2, operation)
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

print("Thank you for trying this out with Group ONE!")
