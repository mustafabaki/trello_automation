import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def load_commits():
    # Authentication: replace with your GitHub access token or username/password
    auth = ('access_token', os.environ["GITHUB_TOKEN"])
    # or auth = ('username', 'password')

    # Repository information: replace with your repository details
    owner = os.environ['GITHUB_OWNER']
    repo = os.environ['GITHUB_REPO']

    # API endpoint for getting commits
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    # Parameters for API request: get last  commit
    params = {'per_page': 1}

    # Make the API request
    response = requests.get(url, params=params, auth=auth)

    commit_messages = []

    # Check if response was successful
    if response.status_code == requests.codes.ok:
        # Extract commit data from response JSON
        commits = response.json()
        for commit in commits:
            # Extract relevant commit information
            message = commit['commit']['message']
            commit_messages.append(message)
    else:
        print(f'Request failed with status code {response.status_code}')
        print(f'Debug information:\n{response.json()["message"]}')

    return commit_messages
