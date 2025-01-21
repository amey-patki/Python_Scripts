import requests

def download_file(url, local_filename):
    print(f"Downloading file from {url}...")
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {local_filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Example usage with a working URL
url = 'https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore'  # Example URL for a .gitignore file
local_filename = 'Python.gitignore'
download_file(url, local_filename)
