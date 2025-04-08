# Read a file, modify its content, and write to a new file
def read_and_write_file(input_file, output_file):
    try:
        # Open and read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Content has been modified and written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = "input.txt"
output_filename = "modified_output.txt"
read_and_write_file(input_filename, output_filename)
