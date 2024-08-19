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

# POST request to the specified endpoint URL with a GraphQL query (read in file) and headers, returning the response
def run_query(query):
    response = requests.post(
        url,
        json={
            "query": query,
            "variables": {"num_repos": 1, "num_issues": 3}
        },
        headers=headers
    )
    return response

def display_data(response):
    if response.status_code == 200:
        data = response.json()
        print("# All Issues:")
        print(data)
    else:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")

print(""" 
    Select query:
    1 - Closed issues
    2 - All issues
""")
option = input("Option: ")
match option:
    case '1':
        response = run_query(closed_issues_query)
        display_data(response)
    case '2':
        response = run_query(all_issues_query)
        display_data(response)