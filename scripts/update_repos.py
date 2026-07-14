import os
import requests
import random

# --- Configurações ---
GITHUB_USERNAME = "antoniomalheirs"
NUM_REPOS = 4
CARD_PARAMS = "theme=onedark&hide_border=true&hide_title=false&show_icons=true"

README_TEMPLATE = """<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=91B674&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=D86D73&size=35&center=true&vCenter=true&width=1000&lines=Hello+World,+My+name+is+Anthony+José.!;I'm+24+years+old;I'm+from+Brazil+💻👨‍💻🚀💡🇧🇷✨)](https://git.io/typing-svg)

```text
 .----------------.   .----------------.   .----------------.   .----------------.   .----------------.   .---------------.
| .--------------. | | .--------------. | | .--------------. | | .--------------. | | .--------------. | | .-------------. |
| |  _______     | | | |  _________   | | | |      __      | | | |  _________   | | | | ____    ____ | | | |  _________  | |
| | |_   __ \    | | | | |_   ___  |  | | | |     /  \     | | | | |   ____  \  | | | ||_   \  /   _|| | | | |_   ___  | | |
| |   | |__) |   | | | |   | |_  \_|  | | | |    / /\ \    | | | | |  |    \ |  | | | |  |   \/   |  | | | |   | |_  \_| | |
| |   |  __ /    | | | |   |  _|  _   | | | |   / ____ \   | | | | |  |    |  | | | | |  | |\  /| |  | | | |   |  _|  _  | |
| |  _| |  \ \_  | | | |  _| |___/ |  | | | | _/ /    \ \_ | | | | |  |____/ |  | | | | _| |_\/_| |_ | | | |  _| |___/ | | |
| | |____| |___| | | | | |_________|  | | | ||____|  |____|| | | | |_________/  | | | ||_____||_____|| | | | |_________| | |
| |              | | | |              | | | |              | | | |              | | | |              | | | |             | |
| '--------------' | | '--------------' | | '--------------' | | '--------------' | | '--------------' | | '-------------' |
 '----------------'   '----------------'   '----------------'   '----------------'   '----------------'   '---------------'
==========================================================================================================================
|                                                        About Me                                                        |
==========================================================================================================================
```
<div align="center">
  <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
    <tr style="border: none;">
      <td width="60%" align="left" valign="middle" style="border: none; padding: 10px;">
        <ul>
          <li><b>Bacharel em Ciência da Computação</b>
            <ul>
              <li>Faculdade Adamantinense Integrada (FAI)</li>
            </ul>
          </li>
          <br>
          <li><b>Técnico em Redes de Computadores e Infraestrutura</b>
            <ul>
              <li>Etec Prof. Eudécio Luiz Vicente - Centro Paula Souza</li>
            </ul>
          </li>
        </ul>
      </td>
      <td width="40%" align="center" valign="middle" style="border: none; padding: 20px;">
          <a href="https://www.instagram.com/malheirosan" target="_blank"><img align="center" src="https://raw.githubusercontent.com/Kourva/AwesomeBadges/main/Badges/social/instagram.png" alt="Instagram" width="80" style="margin: 5px;"/></a>
          <a href="https://discord.com/users/ID" target="_blank"><img align="center" src="https://raw.githubusercontent.com/Kourva/AwesomeBadges/main/Badges/social/discord.png" alt="Discord" width="80" style="margin: 5px;"/></a>
          <br>
          <a href="https://t.me/unkandata" target="_blank"><img align="center" src="https://raw.githubusercontent.com/Kourva/AwesomeBadges/main/Badges/social/telegram.png" alt="Telegram" width="80" style="margin: 5px;"/></a>
          <a href="https://www.linkedin.com/in/SEU-USUARIO-AQUI" target="_blank"><img align="center" src="https://raw.githubusercontent.com/Kourva/AwesomeBadges/main/Badges/social/linkedin.png" alt="Linkedin" width="80" style="margin: 5px;"/></a>
      </td> 
    </tr>
    <tr style="border: none;">
      <td colspan="2" style="border: none; padding: 0; line-height: 0;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Transparent.gif" width="800" height="1" alt="" />
      </td>
    </tr>
  </table>
</div>

<!--START_SECTION:waka-->
<!--END_SECTION:waka-->

```text
  .--------------------------------------------------------------------------------------------------------------------.
 | /   \                                                                                                          /   \ |
| | .-. |                                                                                                        | .-. | |
| | | | |                            ♫    S K I L L S,  S T A T S  &  M U S I C    ⚙                             | | | | |
| | '-' |                                                                                                        | '-' | |
 | \   /                                                                                                          \   / |
  '--------------------------------------------------------------------------------------------------------------------'
```
<div align="center">
  <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
    <tr style="border: none;">
      <td width="38%" align="center" valign="middle" style="border: none; padding: 10px;">
        <img src="https://github-stats-alpha.vercel.app/api?username=antoniomalheirs&cc=292C34&tc=CD6D73&ic=91B674&bc=292C34" width="100%" alt="GitHub Stats_Profile">
        <br><br>
        <img src="https://github-readme-streak-stats.herokuapp.com?user=antoniomalheirs&theme=onedark&hide_border=true" width="100%" alt="GitHub Streak">
      </td>
      <td width="24%" align="center" valign="middle" style="border: none; padding: 10px;">
        <img src="https://spotify-recently-played-readme.vercel.app/api?user=zeca09&width=300&count=5" width="100%" alt="Spotify Recently Played"/>
      </td> 
      <td width="38%" align="center" valign="middle" style="border: none; padding: 10px;">
        <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=antoniomalheirs&show_icons=true&theme=onedark&hide_border=true&hide_title=false" width="100%" alt="GitHub Stats_Profile_Two">
        <br><br>
        <img src="https://streak-stats.demolab.com/?user=antoniomalheirs&theme=onedark&hide_border=true&mode=weekly" width="100%" alt="GitHub Streak_Week" />
      </td>
    </tr>
  </table>
</div>

```text
o------------------------------------------------------------------------------------------------------------------------o
|  [+]                                                                                                              [+]  |
|  [+]                                   T O O L I N G   &   A B I L I T I E S                                      [+]  |
|  [+]                                                                                                              [+]  |
o------------------------------------------------------------------------------------------------------------------------o
```
<div align="center">
  <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
    <tr style="border: none;">
      <td width="30%" align="center" valign="middle" style="border: none; padding: 15px;">
        <h4>Programming Languages</h4>
        <img src="https://skillicons.dev/icons?i=java,js,c,cpp,cs,py,bash&perline=4" alt="Programming Languages"/>
        <br><br>
        <h4>Web & Backend Development</h4>
        <img src="https://skillicons.dev/icons?i=nodejs,npm,express,tailwind,mongodb,mysql,firebase,sqlite&perline=4" alt="Web & Backend Development"/>
      </td>
      <td width="40%" align="center" valign="middle" style="border: none; padding: 15px;">
        <img src="./public/top-languages.gif" width="420" height="230" alt="Dynamic Top Languages">
        <br><br>
        <img src="./public/stats.gif" width="380" height="230" alt="Dynamic Top Stats">
      </td>
      <td width="30%" align="center" valign="middle" style="border: none; padding: 15px;">
        <h4>Tools & Platforms</h4>
        <img src="https://skillicons.dev/icons?i=git,github,githubactions,androidstudio,gcp,vscode,visualstudio,linux&perline=4" alt="Tools & Platforms"/>
        <br><br>
        <h4>Other Skills</h4>
        <img src="https://skillicons.dev/icons?i=discordjs,bots,unity,arduino,&perline=4" alt="Other Skills"/>
      </td>
    </tr>
  </table>
</div>

```text
<////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////>
|                                                                                                                        |
|                                      K N O W L E D G E   O F   L A N G U A G E S                                       |
|                                                                                                                        |
<////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////>
```
<div align="center">
    <img src="./profile-3d-contrib/profile-night-rainbow.svg" alt="3D Contribution Graph"/>
</div>
<br>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/antoniomalheirs/antoniomalheirs/output/github-contribution-grid-snake.svg">
  </picture>
</p>

```text
   ____________________________________________________________________________________________________________________
 /    ______________________________________________________________________________________________________________   \\ 
|  //                                                                                                               |   |
| |                             S O M E   I N T E R E S T I N G   R E P O S I T O R I E S                           |   |
| |_________________________________________________________________________________________________________________/   |
 \\______________________________________________________________________________________________________________________/
```

{repo_section}

<br>
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
    url = f"https://github-readme-stats-eight-theta.vercel.app/api/pin/?username={GITHUB_USERNAME}&repo={repo_name}&{CARD_PARAMS}"
    link = f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
    return f'<a href="{link}"><img src="{url}" alt="{repo_name}" width="400" style="margin: 5px;"/></a>'

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
                    line += "\n  " + generate_repo_markdown(repo2)

                markdown_lines.append(line)

            repo_cards_markdown = "\n  <br/>\n  ".join(markdown_lines)
            repo_cards_markdown = f'<div align="center">\n  {repo_cards_markdown}\n</div>'

    # Preenche o template com a seção de repositórios gerada
    final_readme = README_TEMPLATE.format(repo_section=repo_cards_markdown)

    # Escreve o conteúdo final no arquivo README.md, sobrescrevendo completamente o antigo
    with open("README.md", "w", encoding='utf-8') as f:
        f.write(final_readme)

    print("README.md reescrito com sucesso a partir do template final!")
