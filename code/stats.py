from datetime import date, datetime, timezone
import pandas as pd
import ast
import json

basic_data = pd.read_csv('queries/results/results-0.csv')       # id, name, stars, createdAt, updatedAt, primaryLanguage
issues_data = pd.read_csv('queries/results/results-1.csv')      # id, name, stars, createdAt, updatedAt, primaryLanguage, issues
prs_data = pd.read_csv('queries/results/results-2.csv')         # id, name, stars, createdAt, updatedAt, primaryLanguage, pullRequests
releases_data = pd.read_csv('queries/results/results-2.csv')    # id, name, stars, createdAt, updatedAt, releases, primaryLanguage

# RQ_01
def rq_01(basic_data):
    repo_age = []
    today = datetime.today().date()

    for created_at_date in basic_data['createdAt']:
        date_obj = datetime.fromisoformat(created_at_date.replace('Z', '+00:00')).date()
        age_in_days = today - date_obj
        repo_age.append(age_in_days.days)

    created_at_median = pd.Series(repo_age).median()
    return created_at_median

# RQ_02
def rq_02(prs_data):
    merged_count = []

    for pr in prs_data['pullRequests']:
        pr_data = ast.literal_eval(pr)
        merged_count.append(pr_data['totalCount'])
    
    merged_pull_requests_median = pd.Series(merged_count).median()
    return merged_pull_requests_median

# RQ_03
def rq_03(releases_data):
    total_releases = []

    for release in releases_data['releases']:
        release_data = ast.literal_eval(release)
        total_releases.append(release_data['totalCount'])
        
    total_releases_mean = pd.Series(total_releases).mean()
    return total_releases_mean

# RQ_04
def rq_04(basic_data):
    minutes_since_update = []
    now = datetime.now(timezone.utc)

    for last_updated_date in basic_data['updatedAt']:
        date_obj = datetime.fromisoformat(last_updated_date.replace('Z', '+00:00'))
        time_difference = now - date_obj

        minutes = time_difference.total_seconds() / 60 # Seconds -> minutes
        minutes_since_update.append(minutes)

    updated_at_median = pd.Series(minutes_since_update).median()
    return updated_at_median.round()

# RQ_05
# main_language_median

# RQ_06
# closed_issues_ratio_median