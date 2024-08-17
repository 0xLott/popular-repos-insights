from dotenv import load_dotenv
import os
import requests

# Load .env variables and get GitHub API token
load_dotenv()
token = os.getenv('GITHUB_TOKEN')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# GitHub GraphQL API endpoint
url = "https://api.github.com/graphql"

# Read GraphQL query files
with open("code/queries/all_issues_query.gql", "r") as file:
    all_issues_query = file.read()
with open("code/queries/closed_issues_query.gql", "r") as file:
    closed_issues_query = file.read()

# Send request
response = requests.post(
    url,
    json={
        "query": closed_issues_query,
        "variables": {"num_repos": 99, "num_issues": 3}
    },
    headers=headers
)

if response.status_code == 200:
    data = response.json()
    print("# Closed Issues:")
    print(data)
else:
    raise Exception(f"Failed to fetch repositories: {response.status_code}")

# Send request
response = requests.post(
    url,
    json={
        "query": all_issues_query,
        "variables": {"num_repos": 99, "num_issues": 100}
    },
    headers=headers
)

if response.status_code == 200:
    data = response.json()
    print("# All Issues:")
    print(data)
else:
    raise Exception(f"Failed to fetch repositories: {response.status_code}")
