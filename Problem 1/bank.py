def main():
    # Prompt the user for a greeting
    greeting = input("Please enter your greeting: ").strip().lower()

    # Check the greeting and determine the dollar amount
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# Run the main function
if __name__ == "__main__":
    main()
