import os

def rename_files_with_prefix(prefix):
    # Get the current working directory
    current_directory = os.getcwd()

    # Get the name of the Python script file
    script_name = os.path.basename(__file__)

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Iterate through each file in the directory
    for file_name in files:
        # Check if the item is a file and not the script file
        if os.path.isfile(file_name) and file_name != script_name:
            # Split the file name and extension
            name, extension = os.path.splitext(file_name)

            # Create the new file name with the user-defined prefix
            new_name = f"{prefix}_{name}{extension}"

            # Rename the file
            os.rename(file_name, new_name)

            print(f"Renamed: {file_name} to {new_name}")

if __name__ == "__main__":
    # Get user input for the prefix
    user_prefix = input("Enter the prefix to add to the files: ")

    # Call the function to rename files with the user-defined prefix
    rename_files_with_prefix(user_prefix)

