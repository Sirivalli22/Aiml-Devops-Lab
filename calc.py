# Function to perform operations
def calculate():
    print("--- Simple Python Calculator ---")
    
    # 1. Get user input for numbers and operator
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # 2. Perform the calculation based on the operator
        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            # Error handling for division by zero
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator! Please use +, -, *, or /.")
            
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculate()

