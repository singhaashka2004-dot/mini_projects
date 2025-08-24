# calculator.py

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division by zero
    division = "undefined (division by zero)" if num2 == 0 else num1 / num2

    # Display results
    print("\nResults:")
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")


if __name__ == "__main__":
    main()
