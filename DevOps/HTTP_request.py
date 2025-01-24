import requests

response= requests.get("https://api.github.com")

if response.status_code == 200:
    print("Response Json:")
    print(response.json())
    
else:
    print(f"Failed to retrieve data from the API. Status code: {response.status_code}")