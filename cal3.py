def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Enter 'exit' to end the program.")

    while True:
        # Take user input
        operation = input("Enter operation (+, -, *, /): ")

        # Check if the user wants to exit
        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Take two numbers as input
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the operation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please enter +, -, *, or /")
                continue

            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
