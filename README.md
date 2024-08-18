# popular-repos-insights

A data-driven analysis of the top 1,000 starred open-source GitHub repositories to determine whether high-profile projects display a higher rate of closed issues.

## Examined metrics

1. `all_issues`: total amount of issues from top 1,000 GitHub repos
2. `closed_issues`: amount of closed issues from top 1,000 GitHub repos
3. `closed_issues_ratio`: closed-issues ratio, defined by:
  ```math
    closed\_issues\_ratio = \frac{closed\_issues}{all\_issues}
  ```
---

# Getting Started

## 1. Virtual Environment setup

1.1. Create a virtual environment in the root directory of your project

```bash
python3 -m venv .venv
```

1.2. Activate the virtual environment to use the isolated Python environment

```bash
# On Windows:
source code\.venv\bin\activate
```

```bash
# On Linux or MacOS:
code\.venv\Scripts\activate
```

1.3. With the virtual environment active, install the required packages

```bash
pip install requests
```

```bash
python -m pip install python-dotenv
```

## 2. Run

2.1. Activate the virtual environment

```bash
# On Windows:
source code\.venv\bin\activate
```

```bash
# On Linux or MacOS:
code\.venv\Scripts\activate
```

2.2. Run main.py

```bash
python3 code/main.py
```

---
