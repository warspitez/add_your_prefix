# add_your_prefix
The program assumes that the files to be renamed are in the same directory as the Python script. The program uses os.path.dirname(os.path.abspath(__file__)) to get the absolute path of the directory where the script is located. You can place this script in the folder you want to rename files in and run it from there.

The program prompts the user to enter the prefix they want to add to the file names. The program also assumes that the files have one of the extensions specified in the extensions list. You can add or remove extensions as needed.

The program renames the files based on the prefix entered by the user and a unique number, in the format prefix_count.extension. The count variable is used to ensure that each file has a unique name.
