"""Code to fetch the repository and commits"""

import requests
import json


def get_repo_details(user_name):
    """Fetched the repository"""
    result = []

    user_url = 'https://api.github.com/users/{user_name}/repos'
    
    result.append('User: {user_name}')

    try:
        res = requests.get(user_url)
    except (TypeError, KeyError, IndexError):
        return "unable to fetch user's repos"

    repos = json.loads(res.text)

    try:
        for repo in repos:
            repo_name = repo['name']
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name)
            repo_detail = requests.get(repo_url)
            repo_detail_json = json.loads(repo_detail.text)
            result.append(f'Repo: {repo_name} Number of commits: {len(repo_detail_json)}')
    except (TypeError, KeyError, IndexError):
        return "unable to fetch user's commits"

    return result

def main():
    """Takes user input and calls the main funct"""
    usr_name = input("Enter name of the user = ")

    for repo in get_repo_details(usr_name):
        print(repo)


if __name__ == '__main__':
    main()
