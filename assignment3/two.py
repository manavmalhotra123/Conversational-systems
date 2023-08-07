def calculator():
    while True:
        expression = input("Enter a mathematical expression (or 'exit' to quit): ")

        if expression.lower() == 'exit':
            print("Exiting the calculator.")
            break

        try:
            result = eval(expression)
            print("Result:", result)

        except (SyntaxError, NameError, ValueError):
            print("Invalid expression. Please enter a valid mathematical expression.")

if __name__ == "__main__":
    print("Interactive Python Calculator")
    print("Enter a mathematical expression or type 'exit' to quit.")

    calculator()
