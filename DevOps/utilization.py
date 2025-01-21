import psutil

def check_disk_usage():
    disk_usage=psutil.disk_usage('/')
    used_percent=disk_usage.percent
    
    print(f"Disk usage %: {used_percent  }%")
    
    return used_percent

if __name__ == "__main__":
    check_disk_usage()
