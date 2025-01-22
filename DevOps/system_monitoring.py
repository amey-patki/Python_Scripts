import psutil

def system_metrics():
    cpu_usage=psutil.cpu_percent(interval=1)
    memeory_info=psutil.virtual_memory()
    disk_info=psutil.disk_usage('/')
    
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memeory_info.percent}%")
    print(f"Disk Usage: {disk_info.percent}%")
    
system_metrics()