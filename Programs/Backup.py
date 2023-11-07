import shutil
import datetime

# Define the source directory to be backed up
source_dir = "/path/to/source_directory"

# Create a timestamp for the backup folder
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_dir = f"/path/to/backup_directory/backup_{timestamp}"

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
