import os
# Open the file in read mode
file_path = "/workspaces/Python_Scripts/Programs/Hello"  # Replace with the path to your text file

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print("Contents of the file:")
        print(content)
else:
    print(f"The file '{file_path}' was not found.")
