def camel_to_snake(name):
    snake_case = ""
    for c in name:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    return snake_case

def main():
    # Prompt the user for a camel case variable name
    camel_case_name = input("Enter a camel case variable name: ")

    # Convert to snake case
    snake_case_name = camel_to_snake(camel_case_name)

    # Output the snake case variable name
    print(snake_case_name)

# Ensure the main function is called
if __name__ == "__main__":
    main()
