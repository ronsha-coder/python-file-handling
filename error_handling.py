# Ask the user for a filename and handle errors if it doesn't exist or can't be read
def get_file_content():
    filename = input("Please enter the filename: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: The file {filename} could not be read.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
get_file_content()
