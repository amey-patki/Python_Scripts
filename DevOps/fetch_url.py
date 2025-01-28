import requests

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"failed to fetch data : {response.status_code}")
        return None
    
    
api_url = "https://api.github.com/users/octocat/repos"
data = fetch_url(api_url)
if data:
    for repo in data:
        print(repo["name"])