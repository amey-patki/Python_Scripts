import psutil
from datetime import datetime

# Function to get system resource usage
def system_metrics(log_file):
    # Get CPU, memory, and disk usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Format the log message
    log_message = (
        f"{timestamp} - CPU Usage: {cpu_usage}%\n"
        f"{timestamp} - Memory Usage: {memory_info.percent}%\n"
        f"{timestamp} - Disk Usage: {disk_info.percent}%\n"
        "----------------------------\n"
    )

    # Open the log file in append mode and write the log message
    with open(log_file, 'a') as f:
        f.write(log_message)
    print(f"Logged system metrics to {log_file}")

# Log file path (You can change this to any location you prefer)
log_file_path = "system_metrics.log"

# Call the function to log system metrics
system_metrics(log_file_path)
