import os

def list_files_in_folders(folder_path):
    try:
        files=os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None ,"Folder Not Found"
    except PermissionError:
        return None, "Permission Denied"

def main():
    folder_path=input("Enter list of folder paths seperated by spaces :").split()

    for folder in folder_path:
        files, error_message= list_files_in_folders(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
