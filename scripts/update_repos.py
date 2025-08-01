import os
import requests
import random

# --- Configurações ---
GITHUB_USERNAME = "antoniomalheirs"
NUM_REPOS = 4
CARD_PARAMS = "theme=onedark&hide_border=true&hide_title=false&show_icons=true"
# ---------------------

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

def update_readme_section(new_content):
    """Atualiza a seção de repositórios no README.md, lendo e editando o arquivo."""
    readme_path = "README.md"
    start_marker = ""
    end_marker = ""
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Encontra os números das linhas dos marcadores
        start_index = -1
        end_index = -1
        for i, line in enumerate(lines):
            if start_marker in line:
                start_index = i
            if end_marker in line:
                end_index = i
                break
        
        if start_index == -1 or end_index == -1:
            print(f"Erro: Marcadores para 'pinned_repos' não encontrados no README.md.")
            return

        # Constrói o novo conteúdo do README
        new_readme_lines = lines[:start_index + 1]
        new_readme_lines.append(new_content + '\n')
        new_readme_lines.extend(lines[end_index:])

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(new_readme_lines)
            
        print("Seção de repositórios aleatórios atualizada com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo {readme_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o README: {e}")

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
    
    # Chama a função de atualização que agora edita em vez de reescrever
    update_readme_section(repo_cards_markdown)
