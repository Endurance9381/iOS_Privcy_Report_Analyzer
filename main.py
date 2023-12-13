import json

# Function to upload and parse the file
def upload_and_parse_file():

    # Get the file path from the user
    file_path = input("Enter the absolute path of the text file: ")

    try:
        # Open the file and read its content
        with open(file_path, 'r') as file:
            file_content = file.read()

            # Parse the file content
            lines = file_content.split('\n')

            return lines

    # Handle the exception if a file is Not Found
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")

# Main block
if __name__ == "__main__":

    # Call the function to upload and parse the file
    parsed_file = upload_and_parse_file()

    # Prompt the user to enter the KEY in JSON they want to search
    search_key = input("Enter the KEY in JSON you want to search: ")

    # Iterate over each line in the parsed file
    for i in parsed_file:
        try:
            # Load each line as JSON data
            data = json.loads(i)

            # Print the value associated with the key
            print(data[search_key])

        # Handle JSON decoding errors
        except json.JSONDecodeError as e:
            None

        # Handle KeyError if the key is not found in the JSON
        except KeyError:
            print("No KEY with that name")

