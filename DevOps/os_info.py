import platform
import socket

# Fetching system details
hostname = socket.gethostname()
os_name = platform.system()
os_version = platform.version()

print(f"Hostname: {hostname}")
print(f"Operating System: {os_name}")
print(f"OS Version: {os_version}")
