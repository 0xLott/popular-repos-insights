from dotenv import load_dotenv
import os, requests

# Load .env variables and get GitHub API token
load_dotenv()
token = os.getenv('GITHUB_TOKEN')

headers = {
    "Authorization": f"Bearer {token}"
}

# GitHub GraphQL API endpoint
url = "https://api.github.com/graphql"

# Read GraphQL query files
try:
    with open('code/queries/all_issues_query.gql', 'r') as file:
        all_issues = file.read()
    with open('code/queries/all_issues_query.gql', 'r') as file:
        closed_issues = file.read()
except FileNotFoundError as e:
    print(f"File not found error: {e}")

# Send request
response = requests.get(url, json={'query': closed_issues}, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    raise Exception(f"Failed to fetch repositories: {response.status_code}")

