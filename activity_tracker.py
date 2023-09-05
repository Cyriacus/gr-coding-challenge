import requests
    
# To gather data from GitHub repository 
def get_repository_data(repo_owner, repo_name):
    base_url = f"https://github.com/Cyriacus/gr-coding-challenge.git/{repo_owner}/{repo_name}"
    base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    # to get the commits made by the contributors
    commits_url = f"{base_url}/commits"
    commits_response = requests.get(commits_url, headers=headers)
    commits_data = commits_response.json()

    # to get a pull requests made by the contributors
    pr_url = f"{base_url}/pulls"
    pr_response = requests.get(pr_url, headers=headers)
    pr_data = pr_response.json()

    return {
        "commits": commits_data,
        "pull_requests": pr_data
    }
# to print out the retrieved data
if __name__ == "__main__":
    repo_owner = "Cyriacus"
    repo_name = "gr-coding-challenge"

    data = get_repository_data(repo_owner, repo_name)
    print(data)