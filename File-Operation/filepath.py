import os
cwd = os.getcwd()
print(cwd)  # Current working directory

## List files and directories in the current directory
files_and_directories = os.listdir()
print(files_and_directories)

## Create new directory
# new_directory = "package"
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' created successfully!")

## Join paths
dir_name="folder"
file_name="file.txt"
full_path = os.path.join(dir_name, file_name)
print(full_path) 

path = 'example1.txt'
if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f"{path} does not exist")

path = 'example.txt'
if os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print(f"{path} is neither a file nor a directory")