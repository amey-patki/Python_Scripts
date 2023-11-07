import shutil # shutil module simplifies common file and directory tasks, making it easier to work with the file system.
import datetime

# Define the source directory to be backed up
source_dir = "/path/to/source_directory" #replace with your directory path for which you want to create backup

# Create a timestamp for the backup folder
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_dir = f"/path/to/backup_directory/backup_{timestamp}" #backup folder

try:
    # Copy the contents of the source directory to the backup directory
    shutil.copytree(source_dir, backup_dir)
    print(f"Backup created successfully at {backup_dir}")
except FileNotFoundError:
    print(f"Source directory not found.")
except FileExistsError:
    print(f"Backup directory already exists.")
except Exception as e:
    print(f"An error occurred: {e}")


