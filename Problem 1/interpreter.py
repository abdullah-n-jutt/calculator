def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ").strip()

    # Split the expression into components
    x, y, z = expression.split(" ")

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the calculation based on the operator y
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Invalid operator")
        return

    # Print the result formatted to one decimal place
    print(f"{result:.1f}")

# Run the main function
if __name__ == "__main__":
    main()
