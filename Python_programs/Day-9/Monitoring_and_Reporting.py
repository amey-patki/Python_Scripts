import psutil  # Import the psutil library for system resource information

def monitor_server_resources(server_name):
    try:
        # Get CPU and memory usage information using psutil
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()

        # Simulate printing the monitoring results
        print(f"Server: {server_name}")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_info.percent}%")
        print("")

    except Exception as e:
        print(f"Error monitoring server {server_name}: {e}")

# List of server names or IP addresses
servers = ['Server1', 'Server2', 'Server3']

# Monitor resources on each server using a for loop
for server in servers:
    monitor_server_resources(server)
