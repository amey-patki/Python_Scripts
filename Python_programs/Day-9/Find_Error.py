<<<<<<< HEAD
# Find Error in log file
=======

>>>>>>> 73002c885514c3f9bd27a54aee917fe625197e76
def analyze_log_file(file_path):
    try:
        # Open the log file in read mode
        with open(file_path, 'r') as log_file:
            # Read each line in the file
            for line_number, line in enumerate(log_file, start=1):
                # Check if the word "error" is present in the line (case-insensitive)
                if "error" in line.lower():
                    # Print the line number and the line containing the error
                    print(f"Error found in line {line_number}: {line.strip()}")

        print("Analysis complete.")
    
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")

# Provide the path to your log file
log_file_path = '/workspaces/Python_Scripts/Python_programs/Day-9/Demo.log'

# Call the function to analyze the log file
analyze_log_file(log_file_path)
