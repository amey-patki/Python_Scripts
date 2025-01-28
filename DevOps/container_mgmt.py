import docker

# List running Docker containers
def list_containers():
    client = docker.from_env()
    containers = client.containers.list()
    containers = client.containers.list(all=True) # Include stopped containers
    for container in containers:
        print(f"Container ID: {container.id}, Name: {container.name}")

# Example usage
list_containers()

