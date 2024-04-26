#!/usr/bin/python3
"""
this script  takes arguments in order to list 10 commits
of the repository "rails" by the user "rails".
"""
import requests
import sys


if __name__ == "__main__":
    repo_owner = sys.argv[2]
    repo_name = sys.argv[1]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        for i in range(min(len(commits), 10)):
            commit = commits[i]
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
