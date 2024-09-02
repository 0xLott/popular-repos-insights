import ast
from collections import Counter
from datetime import datetime, timezone

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# RQ_01
def rq_01(data):
    repo_age = []
    today = datetime.today().date()

    for row in data['createdAt']:
        date_obj = datetime.fromisoformat(row.replace('Z', '+00:00')).date()
        age_in_days = today - date_obj
        repo_age.append(age_in_days.days)

    created_at_median = np.median(repo_age)

    plt.hist(repo_age, bins=30, color='skyblue', edgecolor='black')
    plt.axvline(created_at_median, color='red', linestyle='dashed', linewidth=1)
    plt.title('Distribuição de Idade dos Repositórios')
    plt.xlabel('Idade (Dias)')
    plt.ylabel('Frequência')
    plt.show()

    return created_at_median


# RQ_02
def rq_02(data):
    merged_count = []

    for row in data['pullRequests']:
        pr_data = ast.literal_eval(row)
        merged_count.append(pr_data['totalCount'])

    merged_pull_requests_median = np.median(merged_count)

    plt.hist(merged_count, bins=30, color='lightgreen', edgecolor='black')
    plt.axvline(merged_pull_requests_median, color='red', linestyle='dashed', linewidth=1)
    plt.title('Distribuição de PRs Mergidas')
    plt.xlabel('Numero de PRs Mergidas')
    plt.ylabel('Frequência')
    plt.show()

    return merged_pull_requests_median


# RQ_03
def rq_03(data):
    total_releases = []

    for row in data['releases']:
        release_data = ast.literal_eval(row)
        total_releases.append(release_data['totalCount'])

    total_releases_mean = np.mean(total_releases)

    plt.hist(total_releases, bins=30, color='salmon', edgecolor='black')
    plt.axvline(total_releases_mean, color='red', linestyle='dashed', linewidth=1)
    plt.title('Distribuição do Total de Releases')
    plt.xlabel('Número de Releases')
    plt.ylabel('Frequência')
    plt.show()

    return total_releases_mean


# RQ_04
def rq_04(data):
    minutes_since_update = []
    now = datetime.now(timezone.utc)

    for row in data['updatedAt']:
        date_obj = datetime.fromisoformat(row.replace('Z', '+00:00'))
        time_difference = now - date_obj

        minutes = time_difference.total_seconds() / 60
        minutes_since_update.append(minutes)

    updated_at_median = np.median(minutes_since_update)

    plt.hist(minutes_since_update, bins=30, color='orange', edgecolor='black')
    plt.axvline(updated_at_median, color='red', linestyle='dashed', linewidth=1)
    plt.title('Distribuição de Minutos Desde a Ultima Atualização')
    plt.xlabel('Minutos')
    plt.ylabel('Frequência')
    plt.show()

    return np.round(updated_at_median)


# RQ_05
def rq_05(data):
    languages = []

    for row in data['primaryLanguage']:
        if pd.isna(row):
            continue

        lang_data = ast.literal_eval(row)
        languages.append(lang_data['name'])

    language_counts = Counter(languages)

    plt.figure(figsize=(12, 8))
    plt.bar(language_counts.keys(), language_counts.values(), color='purple', width=0.7)

    plt.title('Distribuição de Linguagens de Programação Primarias')
    plt.xlabel('Linguagem')
    plt.ylabel('Contagem')

    plt.xticks(rotation=45, ha='right', fontsize=10)

    # Espaçamento
    plt.gca().margins(x=0.01)
    plt.subplots_adjust(bottom=0.2)

    plt.show()

    return language_counts


# RQ_06
def rq_06(data):
    total_nodes = 0
    closed_issues_count = 0

    for row in data['issues']:
        issues = ast.literal_eval(row)

        nodes = issues['edges']
        total_nodes += len(nodes)

        closed_issues_count += sum(1 for node in nodes if node['node']['closed'] is True)

    closed_issues_percentage = (closed_issues_count / total_nodes * 100)

    labels = ['Issues Fechadas', 'Issues Abertas']
    sizes = [closed_issues_percentage, 100 - closed_issues_percentage]
    colors = ['lightblue', 'lightcoral']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Issues Abertas x Fechadas')
    plt.show()

    return closed_issues_percentage


if __name__ == '__main__':
    basic_data = pd.read_csv('queries/results/results-0.csv')  # id, name, stars, createdAt, updatedAt, primaryLanguage
    issues_data = pd.read_csv('queries/results/results-1.csv')  # id, name, stars, createdAt, updatedAt, primaryLanguage, issues
    prs_data = pd.read_csv('queries/results/results-2.csv')  # id, name, stars, createdAt, updatedAt, primaryLanguage, pullRequests
    releases_data = pd.read_csv('queries/results/results-2.csv')  # id, name, stars, createdAt, updatedAt, releases, primaryLanguage

    rq_01(basic_data)
    rq_02(prs_data)
    rq_03(releases_data)
    rq_04(basic_data)
    rq_05(basic_data)
    rq_06(issues_data)
