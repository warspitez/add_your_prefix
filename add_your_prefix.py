import os

def get_valid_prefix():
    while True:
        prefix = input("Enter the prefix to add to the files: ")
        if prefix.strip():  # Ensure non-empty prefix
            return prefix
        else:
            print("Prefix cannot be empty. Please try again.")

if __name__ == "__main__":
    # Get user input for the prefix
    user_prefix = input("Enter the prefix to add to the files: ")

    # Call the function to rename files with the user-defined prefix
    rename_files_with_prefix(user_prefix)

