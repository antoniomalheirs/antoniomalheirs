import os
import requests
import random

# --- Configurações ---
GITHUB_USERNAME = "antoniomalheirs"
NUM_REPOS = 4
CARD_PARAMS = "theme=onedark&hide_border=true&hide_title=false&show_icons=true"

# --- Template do README (VERSÃO FINAL COM BANNERS LARGOS E CENTRALIZADOS) ---
# Este template está com a indentação e a estrutura corrigidas para funcionar perfeitamente.
README_TEMPLATE = """<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=91B674&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=D86D73&size=35&center=true&vCenter=true&width=1000&lines=Hello+World,+My+name+is+Anthony+José.!;I'm+24+years+old;I'm+from+Brazil+💻👨‍💻🚀💡🇧🇷✨)](https://git.io/typing-svg)

```text
                                        ___       ___           ___           ___           ___     
                                      /  /\     /  /\         /  /\         /  /\         /  /\    
                                      /  /:/_   /  /::\       /  /::\       /  /::\       /  /::\   
                                    /  /:/ /\ /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\  
                                    /  /:/ /:/ /  /:/~/::\   /  /:/  \:\   /  /:/~/::\   /  /:/  \:\ 
                                  /__/:/ /:/ /__/:/ /:/\:\ /__/:/ \__\:\ /__/:/ /:/\:\ /__/:/ \__\:\:
                                  \__\/ /:/  \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:/__\/ \  \:\ /  /:/
                                    /  /:/    \  \::/       \  \:\  /:/   \  \::/       \  \:\  /:/ 
                                    /  /:/      \  \:\        \  \:\/:/     \  \:\        \  \:\/:/  
                                  /  /:/        \  \:\        \  \::/       \  \:\        \  \::/   
                                  \__\/          \__\/         \__\/         \__\/         \__\/    
============================================================================================================================
|                                                        About Me                                                          |
============================================================================================================================
```
<p align="center">
  Graduated in Computer Science from Faculdade Adamantinense Integrada - FAI, Technician in Computer Networks/Infras from Etec Prof. Eudécio Luiz Vicente - Center Paula Souza.
</p>

<!--START_SECTION:waka-->
<!--END_SECTION:waka-->

```text
   .---------------------------------------------------------------------------------------------------------------------.
  /  .-.                                                                                                            .-.   \.
 |  /   \                                                                                                          /   \   |
 | |  .-. |                                                                                                        | .-. | |
 | | |   | |                      ♫    S K I L L S   ,   S T A T S   &   M U S I C    ⚙                            | |   | |
 | | |   | |                                                                                                       | |   | |
 | |  '-' |                                                                                                        | '-' | |
 |  \   /                                                                                                           \   /  |
  \  '-'                                                                                                             '-'  /
   '---------------------------------------------------------------------------------------------------------------------'
```
<div align="center">
  <table border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
    <tr style="border: none;">
      <td style="border: none; vertical-align: top; padding-right: 10px;">
        <img src="https://github-stats-alpha.vercel.app/api?username=antoniomalheirs&cc=292C34&tc=CD6D73&ic=91B674&bc=292C34" width="410" alt="GitHub Stats">
        <br> 
        <img src="https://github-readme-streak-stats.herokuapp.com?user=antoniomalheirs&theme=onedark&hide_border=true" width="400" alt="GitHub Streak">
      </td>
      <td style="border: none; vertical-align: top; padding-right: 10px;">
        <img src="https://github-readme-stats.vercel.app/api?username=antoniomalheirs&show_icons=true&theme=onedark&hide_border=true&hide_title=false&include_all_commits=true" width="390" alt="Top Languages">
        <br>
        <img src="https://streak-stats.demolab.com/?user=antoniomalheirs&theme=onedark&hide_border=true&mode=weekly" width="400"  alt="antoniomalheirs" />
      </td>
      <td style="border: none; vertical-align: top; padding-left: 10px;">
        <img src="https://spotify-recently-played-readme.vercel.app/api?user=zeca09&width=300&count=7" alt="Spotify Recently Played"/>
      </td>
    </tr>
  </table>
</div>

```text
o--------------------------------------------------------------------------------------------------------------------------o
|  [+]                                                                                                                [+]  |
|  [+]                                    T O O L I N G   &   A B I L I T I E S                                       [+]  |
|  [+]                                                                                                                [+]  |
o--------------------------------------------------------------------------------------------------------------------------o
```
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

```text
<//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////>
|                                                                                                                          |
|                                          K N O W L E D G E   O F   L A N G U A G E S                                     |
|                                                                                                                          |
<//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////>
```
<div align="center">
    <img src="./profile-3d-contrib/profile-night-rainbow.svg" alt="3D Contribution Graph"/>
</div>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake.svg">
  </picture>
</p>

```text
  ________________________________________________________________________________________________________________________
 /                                                                                                                         \\
|    _________________________________________________________________________________________________________________      |
|   |                                                                                                                 |     |
|   |                           S O M E   I N T E R E S T I N G   R E P O S I T O R I E S                             |     |
|   |_________________________________________________________________________________________________________________|     |
|                                                                                                                           |
 \\_________________________________________________________________________________________________________________________/
```

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

# Bloco de execução principal do script
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
                    line += "\n" + generate_repo_markdown(repo2)

                markdown_lines.append(line)

            repo_cards_markdown = "\n<br><br>\n".join(markdown_lines)
            repo_cards_markdown = f'<div align="center">\n{repo_cards_markdown}\n</div>'

    # Preenche o template com a seção de repositórios gerada
    final_readme = README_TEMPLATE.format(repo_section=repo_cards_markdown)

    # Escreve o conteúdo final no arquivo README.md, sobrescrevendo completamente o antigo
    with open("README.md", "w", encoding='utf-8') as f:
        f.write(final_readme)

    print("README.md reescrito com sucesso a partir do template final!")
