import time  # Import the time module for simulating delays

def backup_database(database_name):
    # Simulate the backup process
    print(f"Backing up database {database_name}... Done!")
    # Simulate a delay (replace this with the actual backup process)

def restore_database(backup_file, destination_database):
    # Simulate the restore process
    print(f"Restoring {backup_file} to database {destination_database}... Done!")
    # Simulate a delay (replace this with the actual restore process)

# List of databases to be backed up and restored
databases = ['DB1', 'DB2', 'DB3']

# Backup each database using a for loop
for database in databases:
    backup_database(database)

# Simulate a delay between backup and restore operations
time.sleep(2)

# Restore each database using a for loop
for database in databases:
    # In a real-world scenario, you would need the backup file and the destination database
    backup_file = f"backup_{database}.bak"
    restore_database(backup_file, database)
