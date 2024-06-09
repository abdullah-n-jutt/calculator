def main():
    # Prompt the user for the name of a file
    file_name = input("Enter the name of a file: ").strip().lower()

    # Define a dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Determine the file extension
    for ext, media_type in media_types.items():
        if file_name.endswith(ext):
            print(media_type)
            return

    # Default media type
    print("application/octet-stream")

# Run the main function
if __name__ == "__main__":
    main()
