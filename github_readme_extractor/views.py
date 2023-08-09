import requests
import markdown
from django.shortcuts import render

def index(request, github_username='prateek271'):
    api_url = f'https://api.github.com/users/{github_username}/repos'
    response = requests.get(api_url)
    repos = response.json()
    repo_img_url=repos[0]['owner']['avatar_url']

    return render(request, 'github_api/index.html', {'repos': repos, 'github_username': github_username, 'repo_img_url': repo_img_url})

def readme_data(request, github_username, repo_name):
    readme_url = f'https://raw.githubusercontent.com/{github_username}/{repo_name}/main/README.md'
    readme_response = requests.get(readme_url)
    
    # Check if the README file exists
    if readme_response.status_code == 200:
        readme_content = readme_response.text

        # Convert Markdown content to HTML
        readme_html = markdown.markdown(readme_content)

        return render(request, 'github_api/data.html', {'readme_html': readme_html})
    else:
        return render(request, 'github_api/data.html', {'readme_html': 'README not found'})
