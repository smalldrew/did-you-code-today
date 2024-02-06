import requests
import util.SMS as SMS
from datetime import date 

GITHUB_USERNAME = 'INSERT YOUR GITHUB USERNAME HERE'
GITHUB_TOKEN = 'INSERT YOUR GITHUB DEVELOPER TOKEN HERE'
GITHUB_API_URL = 'https://api.github.com/'

def _get_github_header(token: str) -> dict:
    """Returns an header with a given token"""
    header = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    return header


def get_github_repositories(username: str, token: str) -> list[str]:
    """Returns a list of all of a user's Github repositories"""
    repository_list = []
    github_header = _get_github_header(token) 
    response = requests.get(f'{GITHUB_API_URL}users/{username}/repos', headers=github_header)

    if not response.status_code == 200:
        return repository_list 
    
    data = response.json()

    print("Repositories:")

    for repo in data:
        repository_list.append(repo["name"]) 
        print(repo["name"])


    return repository_list 


def get_repository_commits(username: str, token: str, repository: str) -> any:
    """Goes through a list of repository list. Returns a list of commits"""
    commit_list = []
    github_header = _get_github_header(token)
    response = requests.get(f'{GITHUB_API_URL}repos/{username}/{repository}/commits')

    if not response.status_code == 200:
        return commit_list
    
    data = response.json()

    for commit in data:
        commit_list.append(commit)

    return commit_list


def committed_today(username, commit) -> bool:
    """Checks if a commit was made on the current date"""
    if not str(date.today()) in commit["commit"]["committer"]["date"]:
        return False 

    if not commit["author"]["login"] == username:
        return False

    return True 


def did_you_code_today(username, token) -> bool:
    """Checks all your public repositories and sees if you committed"""
    commit_status = False

    repository_list = get_github_repositories(username, token)
    for repository in repository_list:
        commit_list = get_repository_commits(username, token, repository)
        for commit in commit_list:
            if committed_today(username, commit):
                commit_status = True
    
    return commit_status 


def check(username, token):
    """Sends a message if you didn't code. Otherwise, it sends a good job message."""
    if did_you_code_today(username, token):
        print('LOG: Sent good job message.')
        SMS.send_text('Good job. You coded today.')
    else:
        print('LOG: Sent angry message.')
        SMS.send_text('GO CODE RIGHT NOW OR YOU WILL DIE.')



if __name__ == '__main__':
    check(GITHUB_USERNAME, GITHUB_TOKEN)
