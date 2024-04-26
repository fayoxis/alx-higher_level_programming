#!/usr/bin/python3
"""
this script  takes arguments in order to list 10 commits
of the repository "rails" by the user "rails".
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repo_owner = sys.argv[2]
        repo_name = sys.argv[1]
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        response = requests.get(url)
        commits = response.json()
        for i in range(min(10, len(commits))):
            commit = commits[i]
            sha = commit.get("sha")
            author_name = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author_name}")
    except (IndexError, KeyError):
        pass
