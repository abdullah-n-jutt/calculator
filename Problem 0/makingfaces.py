def convert(text):
    """
    Convert :) to 🙂 and :( to 🙁 in the given text.

    Args:
    text (str): The input text to be converted.

    Returns:
    str: The converted text.
    """

    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    """
    Main function to prompt the user for input, call convert, and print the result.
    """
    user_input = input("Enter text: ")
    converted_text = convert(user_input)
    print("Converted text:", converted_text)

main()
