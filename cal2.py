# Using "def" Key and also while loop so that calculator won't exit until user ask for it!!

def calculator():
    print("Simple Calculator")
    print("Enter 'exit' to end the program.")

    while True:
        operation = input("Enter operation:\n")
        if operation.lower() == 'exit':
        else operation.upper() == 'EXIT' :
            print("Exiting the calculator. Goodbye!")
            break

        try:
            result = eval(operation) # evaluation to operate the result
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()