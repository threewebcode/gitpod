import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import shutil

TRENDING_URL = "https://github.com/trending"

def fetch_trending_repositories():
    response = requests.get(TRENDING_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    repos = []
    for repo in soup.select('article h2 a'):
        repo_name = repo['href'].strip('/')
        repos.append(repo_name)
    return repos

def create_directory():
    now = datetime.now()
    dir_name = now.strftime("%Y-%m-%d")
    
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        print(f"Directory '{dir_name}' deleted.")
    
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created.")
    
    return dir_name

def clone_repositories(repos, dir_name):
    for repo in repos:
        clone_url = f"https://github.com/{repo}.git"
        repo_dir = os.path.join(dir_name, repo.split('/')[-1]) 
        print(f"Cloning {repo} into {repo_dir}...")
        
        os.system(f"git clone {clone_url} {repo_dir}")

if __name__ == "__main__":
    trending_repos = fetch_trending_repositories()
    print("Trending Repositories:")
    for repo in trending_repos:
        print(repo)
    
    directory_name = create_directory()
    clone_repositories(trending_repos, directory_name)
