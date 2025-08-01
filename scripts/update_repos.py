import os
import requests
import random

# --- Configurações ---
GITHUB_USERNAME = "antoniomalheirs"
NUM_REPOS = 4
CARD_PARAMS = "theme=onedark&hide_border=true&hide_title=false&show_icons=true"

# --- Template do README ---
# Este é o seu layout base, com um marcador {repo_section} onde os repositórios entrarão.
README_TEMPLATE = """
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=91B674&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=D86D73&size=35&center=true&vCenter=true&width=1000&lines=HELLO,+My+name+is+Antonio+Malheiros.!;I'm+24+years+old;I'm+from+Brazil;I+Graduated+on+Computer+Science;And+Tech;+On+Network+Infrastructure.!+:%29)](https://git.io/typing-svg)

### About Me
Graduated in Computer Science from Faculdade Adamantinense Integrada - FAI, Technician in Computer Networks/Infras from Etec Prof. Eudécio Luiz Vicente - Center Paula Souza.

<!--START_SECTION:waka-->
<!--END_SECTION:waka-->

<h3 align="center">Skills, Stats & Music</h3>
<div align="center">
  <table border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
    <tr style="border: none;">
      <td style="border: none; vertical-align: top; padding-right: 10px;">
        <img src="https://github-stats-alpha.vercel.app/api?username=antoniomalheirs&cc=292C34&tc=CD6D73&ic=91B674&bc=292C34" width="400" alt="GitHub Stats">
        <br>
        <img src="https://github-readme-streak-stats.herokuapp.com?user=antoniomalheirs&theme=onedark&hide_border=true" width="400" alt="GitHub Streak">
        <br>
        <img src="https://github-readme-stats.vercel.app/api?username=antoniomalheirs&show_icons=true&theme=onedark&hide_border=true&hide_title=true&include_all_commits=true" width="400" alt="Top Languages">
      </td>
      <td style="border: none; vertical-align: top; padding-left: 10px;">
        <img src="https://spotify-recently-played-readme.vercel.app/api?user=zeca09&width=300&count=7" alt="Spotify Recently Played"/>
      </td>
    </tr>
  </table>
</div>

<h3 align="center">Tooling & Abilities</h3>
<div align="center">
  <table border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
    <tr style="border: none;">
      <td style="border: none; vertical-align: top; padding: 0 10px;">
        <img src="https://skillicons.dev/icons?i=gcp,androidstudio,visualstudio,anaconda,c,express,tailwind,bots,firebase,discord,vscode,github,linux&perline=7" alt="Skills Column 1"/>
      </td>
      <td style="border: none; vertical-align: top; padding: 0 10px;">
        <img src="https://skillicons.dev/icons?i=git,java,unity,py,mongodb,sqlite,nodejs,bash,cs,mysql,js,arduino,cpp&perline=7" alt="Skills Column 2"/>
      </td>
    </tr>
  </table>
</div>

<h3 align="center">Knowledge of Languages</h3>
<div align="center">
    <table border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
      <tr style="border: none;">
        <td style="border: none; vertical-align: top; padding-right: 10px;">
           <img src="./profile-3d-contrib/profile-night-rainbow.svg" alt="3D Contribution Graph"/>
        </td>
      </tr>
  </table>
</div>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake.svg">
  </picture>
</p>

<h3 align="center">Some interesting repositories</h3>
{repo_section}

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=91B674&height=120&section=footer"/>
"""

def get_repos(username):
    """Busca os repositórios de um usuário no GitHub, excluindo forks."""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erro ao buscar repositórios: {response.status_code}")
            return []
        data = response.json()
        if not data:
            break
        repos.extend([repo for repo in data if not repo['fork']])
        page += 1
    return repos

def generate_repo_markdown(repo):
    """Gera a linha de markdown para um card de repositório."""
    repo_name = repo['name']
    url = f"https://github-readme-stats.vercel.app/api/pin/?username={GITHUB_USERNAME}&repo={repo_name}&{CARD_PARAMS}"
    link = f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
    return f'<a href="{link}"><img src="{url}" alt="{repo_name}" width="400"/></a>'

if __name__ == "__main__":
    all_repos = get_repos(GITHUB_USERNAME)
    repo_cards_markdown = ""

    if all_repos:
        num_to_sample = min(NUM_REPOS, len(all_repos))
        if num_to_sample > 0:
            random_repos = random.sample(all_repos, num_to_sample)
            
            markdown_lines = []
            for i in range(0, len(random_repos), 2):
                repo1 = random_repos[i]
                line = generate_repo_markdown(repo1)
                
                if i + 1 < len(random_repos):
                    repo2 = random_repos[i+1]
                    # CORREÇÃO AQUI
                    line += "\n" + generate_repo_markdown(repo2)
                
                markdown_lines.append(line)
            
            # CORREÇÃO AQUI
            repo_cards_markdown = "\n<br><br>\n".join(markdown_lines)
            # CORREÇÃO AQUI
            repo_cards_markdown = f'<div align="center">\n{repo_cards_markdown}\n</div>'

    # Preenche o template com a seção de repositórios gerada
    final_readme = README_TEMPLATE.format(repo_section=repo_cards_markdown)

    # Escreve o conteúdo final no arquivo README.md, sobrescrevendo completamente o antigo
    with open("README.md", "w", encoding='utf-8') as f:
        f.write(final_readme)

    print("README.md reescrito com sucesso a partir do template!")
