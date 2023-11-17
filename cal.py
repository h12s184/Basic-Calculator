while True:
    num1_input = input("Enter First number (type 'exit' to end):\n")

    # Check for exit condition
    if num1_input.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break

    # Convert the user input to an integer
    num1 = int(num1_input)

    num2 = int(input("Enter Second number:\n"))
    opr = input("Select any operator:")

    if opr == '+':
        print(num1 + num2)

    elif opr == '-':
        print(num1 - num2)
    # elif opr== '**':
    #     print()

    elif opr == 'x':
        print(num1 * num2)

    elif opr == '%':
        print(num1 % num2)

    elif opr == '/': # Nesting the else if!
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid operator. Please select +, -, x, %, or /")
