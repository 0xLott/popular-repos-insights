from datetime import date, datetime, timezone
from collections import Counter
import pandas as pd
import ast
import json

# RQ_01
def rq_01(data):
    repo_age = []
    today = datetime.today().date()

    for row in data['createdAt']:
        date_obj = datetime.fromisoformat(row.replace('Z', '+00:00')).date()
        age_in_days = today - date_obj
        repo_age.append(age_in_days.days)

    created_at_median = pd.Series(repo_age).median()
    return created_at_median

# RQ_02
def rq_02(data):
    merged_count = []

    for row in data['pullRequests']:
        pr_data = ast.literal_eval(row)
        merged_count.append(pr_data['totalCount'])
    
    merged_pull_requests_median = pd.Series(merged_count).median()
    return merged_pull_requests_median

# RQ_03
def rq_03(data):
    total_releases = []

    for row in data['releases']:
        release_data = ast.literal_eval(row)
        total_releases.append(release_data['totalCount'])
        
    total_releases_mean = pd.Series(total_releases).mean()
    return total_releases_mean

# RQ_04
def rq_04(data):
    minutes_since_update = []
    now = datetime.now(timezone.utc)

    for row in data['updatedAt']:
        date_obj = datetime.fromisoformat(row.replace('Z', '+00:00'))
        time_difference = now - date_obj

        minutes = time_difference.total_seconds() / 60 # Seconds -> minutes
        minutes_since_update.append(minutes)

    updated_at_median = pd.Series(minutes_since_update).median()
    return updated_at_median.round()

# RQ_05
def rq_05(data):
    languages = []

    for row in data['primaryLanguage']:

        if pd.isna(row):   # isna(): detects missing values (NaN)
            continue

        lang_data = ast.literal_eval(row)
        languages.append(lang_data['name'])

    return Counter(languages)

# RQ_06
def rq_06(data):
    total_nodes = 0
    closed_issues_count = 0

    for row in data['issues']:
        issues = ast.literal_eval(row)
        
        nodes = issues['edges']
        total_nodes += len(nodes)
    
        closed_issues_count += sum(1 for node in nodes if node['node']['closed'] is True)
    
    return (closed_issues_count / total_nodes * 100)


if __name__ == '__main__':
    basic_data = pd.read_csv('queries/results/results-0.csv')       # id, name, stars, createdAt, updatedAt, primaryLanguage
    issues_data = pd.read_csv('queries/results/results-1.csv')      # id, name, stars, createdAt, updatedAt, primaryLanguage, issues
    prs_data = pd.read_csv('queries/results/results-2.csv')         # id, name, stars, createdAt, updatedAt, primaryLanguage, pullRequests
    releases_data = pd.read_csv('queries/results/results-2.csv')    # id, name, stars, createdAt, updatedAt, releases, primaryLanguage

    rq_01(basic_data)
    rq_02(prs_data)
    rq_03(releases_data)
    rq_04(basic_data)
    rq_05(basic_data)
    rq_06(issues_data)
