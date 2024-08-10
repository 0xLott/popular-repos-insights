from dotenv import load_dotenv
import os, requests

# Load .env variables and get GitHub API token
load_dotenv()
token = os.getenv('GITHUB_TOKEN')

print(token)

# Get most popular repos, sorted by number of stars
def get_popular_repos(num_repos):
    url = f"https://api.github.com/search/repositories?q=stars:>0&sort=stars&order=desc&per_page={num_repos}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["items"]
    else:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")
    
get_popular_repos(3)