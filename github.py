import os
import requests
from bs4 import BeautifulSoup

TRENDING_URL = "https://github.com/trending"

def fetch_trending_repositories():
    response = requests.get(TRENDING_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    repos = []
    for repo in soup.select('article h2 a'):
        repo_name = repo['href'].strip('/')
        repos.append(repo_name)
    return repos

def clone_repositories(repos):
    for repo in repos:
        clone_url = f"https://github.com/{repo}.git"
        print(f"Cloning {repo}...")
        os.system(f"git clone {clone_url}")

if __name__ == "__main__":
    trending_repos = fetch_trending_repositories()
    print("Trending Repositories:")
    for repo in trending_repos:
        print(repo)
#    clone_repositories(trending_repos)
