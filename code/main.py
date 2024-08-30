from dotenv import load_dotenv
import csv
import os
import requests

load_dotenv()
token = os.getenv('GITHUB_TOKEN')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# GitHub GraphQL API endpoint
url = "https://api.github.com/graphql"

with open("queries/general_query.gql", "r") as file:
    general_query = file.read()
with open("queries/reduced_query.gql", "r") as file:
    reduced_query = file.read()

def run_query(query, variables):
    variables['cursor'] = ''
    total_repos = variables['num_repos']
    retrieved_data = []

    def process_batch(batch_size):
        variables['num_repos'] = batch_size
        json = dispatch_request(query, variables).json()
        
        # Extract the nodes from the response if it's inside a 'node' key
        nodes = json['data']['search']['edges']
        for node in nodes:
            retrieved_data.append(node['node'])

        variables['cursor'] = json['data']['search']['pageInfo']['endCursor']
        return json

    if total_repos > 100:
        full_batches = total_repos // 100
        remaining_items = total_repos % 100

        for batch_number in range(full_batches):
            print(f'Page {batch_number + 1}')
            process_batch(100)

        if remaining_items > 0:
            print('Last Page:')
            process_batch(remaining_items)
    else:
        process_batch(total_repos)

    write_data(retrieved_data)

def dispatch_request(query, variables):
    response = requests.post(
        url,
        json={
            "query": query,
            "variables": variables
        },
        headers=headers
    )

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    return response

def get_unique_filename(base_path):
    counter = 0
    while True:
        new_filename = f"{base_path.rsplit('.', 1)[0]}-{counter}.csv"
        if not os.path.exists(new_filename):
            return new_filename
        counter += 1

def write_data(json):
    csv_file_path = get_unique_filename('queries/results/results.csv')

    parsed_data = [ast.literal_eval(item) if isinstance(item, str) else item for item in json]

    headers = parsed_data[0].keys()

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(parsed_data)

def option_tree(option):
    match option:
        case '1':
            variables = {
                "num_repos": int(input("Repo Max Quantity: ")),
                "num_issues": int(input("Issues Max Quantity: ")),
                "num_pull_requests": int(input("Pull Requests Max Quantity: ")),
                "num_releases": int(input("Releases Max Quantity: ")),
            }

            issue_input = input("Issues State [OPEN, CLOSED, BOTH]: ").upper()

            if issue_input == "BOTH":
                variables["issue_states"] = ["OPEN", "CLOSED"]
            elif issue_input == "OPEN":
                variables["issue_states"] = ["OPEN"]
            elif issue_input == "CLOSED":
                variables["issue_states"] = ["CLOSED"]

            run_query(general_query, variables)

        case '2':
            variables = {
                "num_repos": int(input("Repo Max Quantity: ")),
            }
            run_query(reduced_query, variables)

if __name__ == '__main__':
    print(""" 
        Select query:
        1 - Complete
        2 - Reduced
    """)

    option = input("Option: ")
    option_tree(option)
