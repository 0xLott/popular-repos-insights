# popular-repos-insights

A data-driven analysis of the top 1,000 starred open-source GitHub repositories to determine development patterns from high-profile projects.

## Examined metrics
### RQ-1: "Os sistemas populares são maduros/antigos?"
*"Are popular systems mature/old?"*
- `created_at_median`: median value of days since creation date of the top 1,000 GitHub repos

### RQ-2: "Os sistemas populares recebem muita contribuição externa?"
*"Do popular systems receive a lot of external contributions?"*
- `merged_pull_requests_median`: median value of number of merged pull requests in the top 1,000 GitHub repos

### RQ-3: "Os sistemas populares lançam releases com frequência?"
*"Do popular systems release frequently?"*
- `total_releases_mean`: mean value of number of releases in the top 1,000 GitHub repos

### RQ-4: "Os sistemas populares são atualizados com frequência?"
*"Are popular systems updated frequently?"*
- `last_updated_median`:  median value of minutes since last update date of the top 1,000 GitHub repos

### RQ-5: "Os sistemas populares são escritos nas linguagens mais populares?"
*"Are popular systems written in the most popular languages?"*
- `main_language`: frequency of primary programming languages used in the top 1,000 GitHub repos

### RQ-6: "Os sistemas populares possuem um alto percentual de issues fechadas?"
*"Do popular systems have a high percentage of closed issues?"*
1. `all_issues`: total amount of issues from top 1,000 GitHub repos
2. `closed_issues`: amount of closed issues from top 1,000 GitHub repos
3. `closed_issues_ratio`: closed-issues ratio, defined by:
  ```math
    closed\_issues\_ratio = \frac{closed\_issues}{all\_issues}
  ```

- `closed_issues_ratio_median`: median of closed-issues ratio from top 1,000 GitHub repos
---

# Getting Started

## 1. Virtual Environment setup

1.1 Navigate to "code" directory
```bash
cd code
```

1.2. Create a virtual environment in the root directory of your project
```bash
python3 -m venv .venv
```

1.3. Activate the virtual environment to use the isolated Python environment
```bash
# On Windows:
source .venv/bin/activate
```

```bash
# On Linux or MacOS:
.venv/Scripts/activate
```

1.4. With the virtual environment active, install the required packages
```bash
pip install -r requirements.txt
```

## 2. Run

2.1 Navigate to "code" directory
```bash
cd code
```

2.2. Activate the virtual environment
- Instructions can be found in step 1.3

2.3. Run program
```bash
python3 main.py
python3 stats.py
```

---
