import os

def get_valid_prefix():
    while True:
        prefix = input("Enter the prefix to add to the files: ")
        if prefix.strip():  # Ensure non-empty prefix
            return prefix
        else:
            print("Prefix cannot be empty. Please try again.")

def rename_files_with_prefix(prefix, target_directory=None):
    if target_directory is None:
        target_directory = os.getcwd()

    # List all files in the specified directory
    files = os.listdir(target_directory)

    # Get the name of the Python script file
    script_name = os.path.basename(__file__)

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
    user_prefix = get_valid_prefix()
    rename_files_with_prefix(user_prefix)
