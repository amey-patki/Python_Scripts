import requests

def download_file(url, local_filename):
    print(f"Downloading file from {url}...")
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {local_filename}")

# Example usage
url = 'https://example.com/sample.txt'
local_filename = 'sample.txt'
download_file(url, local_filename)
