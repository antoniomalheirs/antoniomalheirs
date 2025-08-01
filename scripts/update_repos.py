import os
import requests
import random
import re

# --- Configurações ---
GITHUB_USERNAME = "antoniomalheirs"
NUM_REPOS = 4  # Quantidade de repositórios aleatórios a serem exibidos
# Parâmetros para os cards. Adicione ou remova conforme necessário.
CARD_PARAMS = "theme=onedark&hide_border=true&hide_title=true&show_icons=true"
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
            break
        data = response.json()
        if not data:
            break
        # Filtra para não incluir repositórios que são forks
        repos.extend([repo for repo in data if not repo['fork']])
        page += 1
    return repos

def generate_repo_markdown(repo):
    """Gera a linha de markdown para um card de repositório."""
    repo_name = repo['name']
    url = f"https://github-readme-stats.vercel.app/api/pin/?username={GITHUB_USERNAME}&repo={repo_name}&{CARD_PARAMS}"
    link = f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
    return f'<a href="{link}"><img src="{url}" alt="{repo_name}" width="400"/></a>'

def update_readme(new_content):
    """Atualiza o README.md com o novo conteúdo entre os marcadores."""
    readme_path = "README.md"
    start_marker = ""
    end_marker = ""
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()

        # Constrói o bloco de substituição completo
        replacement_block = f"{start_marker}\n{new_content}\n{end_marker}"

        # Expressão regular para encontrar o bloco inteiro, do marcador de início ao de fim
        pattern = re.compile(f"{re.escape(start_marker)}.*{re.escape(end_marker)}", re.DOTALL)
        
        # Substitui o bloco antigo pelo novo
        new_readme = pattern.sub(replacement_block, readme_content)

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_readme)
            
        print("README.md atualizado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo {readme_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o README: {e}")

if __name__ == "__main__":
    all_repos = get_repos(GITHUB_USERNAME)
    if all_repos:
        # Garante que não tentará amostrar mais repositórios do que o disponível
        num_to_sample = min(NUM_REPOS, len(all_repos))
        random_repos = random.sample(all_repos, num_to_sample)
        
        # Gera o HTML/Markdown para os cards em duas colunas
        markdown_lines = []
        for i in range(0, len(random_repos), 2):
            repo1 = random_repos[i]
            line = generate_repo_markdown(repo1)
            
            # Adiciona o segundo repositório na mesma linha, se existir
            if i + 1 < len(random_repos):
                repo2 = random_repos[i+1]
                line += "\n" + generate_repo_markdown(repo2)
            
            markdown_lines.append(line)
            
        # Junta as linhas de colunas duplas com um espaçamento
        final_markdown = "\n<br><br>\n".join(markdown_lines)
        
        # Adiciona o alinhamento central a todo o bloco
        final_markdown = f'<div align="center">\n{final_markdown}\n</div>'
        
        update_readme(final_markdown)
