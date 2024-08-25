from datetime import date, datetime, timezone
import pandas as pd
import json

data = pd.read_csv('queries/results/results-0.csv')

# RQ_01:
def rq_01(data):
    repo_age = []
    today = datetime.today().date()

    for created_at_date in data.createdAt:
        date_obj = datetime.fromisoformat(created_at_date.replace('Z', '+00:00')).date()
        age_in_days = today - date_obj
        repo_age.append(age_in_days.days)

    created_at_median = pd.Series(repo_age).median()
    return created_at_median

# RQ_02
# merged_pull_requests_median

# RQ_03
# total_releases_median

# RQ_04
def rq_04(data):
    minutes_since_update = []
    now = datetime.now(timezone.utc)

    for last_updated_date in data.updatedAt:
        date_obj = datetime.fromisoformat(last_updated_date.replace('Z', '+00:00'))
        time_difference = now - date_obj

        minutes = time_difference.total_seconds() / 60 # Convert seconds to minutes
        minutes_since_update.append(minutes)

    updated_at_median = pd.Series(minutes_since_update).median()
    return updated_at_median.round()

# RQ_05
# main_language_median

# RQ_06
# closed_issues_ratio_median