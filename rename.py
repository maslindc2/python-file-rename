import os
import sys

def performRename(directory): 
    # Check if the directory exists if not print dne error
    if os.path.isdir(directory):
        # Get a list of all files in the directory
        files = os.listdir(directory)

        # Get the total number of files in the directory
        total_files = len(files)

        # Iterate through all files in the directory and rename them
        for i, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[1]

            # Check to see if the current file has already been renamed before
            if not os.path.exists(directory + str(i+1) + file_extension):
                # Create the new file name
                new_file_name = str(i+1) + file_extension
                
                # Create the full path for the new file
                new_file_path = os.path.join(directory, new_file_name)
                # Rename the file
                os.rename(os.path.join(directory, file_name), new_file_path)
                print(f'Renamed {file_name} to {new_file_name}')

        print(f'Renamed {total_files} files in the directory')
    else:
        print("The provided directory does not exist")

def checkPathStructure(directory):
    if directory[0] == '~':
        directory = directory.replace("~", os.path.expanduser('~'))
    
    # If the directory that was passed does not include a "/" then we need to add one
    if directory[len(directory)-1] != '/':    
        directory = "".join([directory, '/'])
        performRename(directory)
    else:
        performRename(directory)

if __name__ == "__main__":
    
    if(len(sys.argv) == 2): 
        # Get the directory to use if it was passed as an arg
        directory = sys.argv[1]
        
        # Check the input's structure
        checkPathStructure(directory)
    else:
        # If there was no directory passed as an arg then prompt user for one
        directory = input("Enter the directory to rename: ")
        
        # Check the input's structure
        checkPathStructure(directory)
    