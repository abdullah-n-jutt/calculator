def main():
    expression = input("Expression = ")

    x = expression.split(" ")
    y = expression.split(" ")
    z = expression.split(" ")

    x = int(x)
    z = int(z)

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

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
