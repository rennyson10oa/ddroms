import os
import shutil
import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from tqdm import tqdm

def criar_nova_pasta(diretorio_pai):
    nome_nova_pasta = input("Digite o nome da nova pasta: ")
    nova_pasta = os.path.join(diretorio_pai, nome_nova_pasta)

    try:
        os.makedirs(nova_pasta)
        print(f"Pasta '{nome_nova_pasta}' criada com sucesso em {diretorio_pai}")
    except FileExistsError:
        print(f"A pasta '{nome_nova_pasta}' já existe em {diretorio_pai}")

def download_file(url, dest):
    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        try:
            with tqdm(unit='B', unit_scale=True, miniters=1, desc="Downloading", leave=True) as t:
                response = requests.get(url, stream=True)
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024
                for data in response.iter_content(block_size, decode_unicode=True):
                    t.update(len(data))
                    with open(dest, 'ab') as f:
                        f.write(data)
            break  # Se o download for bem-sucedido, saia do loop de tentativas
        except Exception as e:
            print(f"Tentativa {attempt} falhou: {str(e)}")
            if attempt == max_attempts:
                print(f"Atenção: Não foi possível baixar o arquivo após {max_attempts} tentativas. Passando para o próximo.")

def print_centered(text):
    terminal_width, _ = shutil.get_terminal_size()
    padding = (terminal_width - len(text)) // 2
    print(" " * padding + text)
def print_all():
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

# Criar a pasta 'roms' se não existir
pasta_destino = 'roms'
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

url = "https://archive.org/details/ni-romsets"
response = requests.get(url)

if response.status_code == 200:
    print_all()
    print_centered(f"*** Bem-vindo ao programa de baixar roms! ***\n")

    #time.sleep(2)
    print_centered("Isso aqui tem um funcionamento simples,")
    print_centered("você pode baixar ROMs de 1 console específico ou baixar de todos os consoles disponíveis,")
    print_centered("e aí, qual você vai querer?")

    #time.sleep(6)
    resposta_init = input(f"1 - baixar todas as roms \n2 - baixar de consoles específicos\n = ")

    if resposta_init == "1":
        aviso1 = input("Tem que certeza que gostaria de baixar")

        soup = BeautifulSoup(response.text, 'html.parser')

        lista = soup.find('tbody')

        if lista:
            rows = lista.find_all('tr')
            consoles = []

            for row in rows:
                console_cell = row.find('td', height='17')
                cells = row.find_all('td')

                if console_cell:
                    console_name = console_cell.text.strip()
                    consoles.append((console_name, cells))

            for idx, (console_name, _) in enumerate(consoles, start=1):
                    print(f"{idx}. {console_name}")

            for console_name, console_cells in consoles:
                pasta_destino_console = os.path.join(pasta_destino, console_name)
                print(f"\nBaixando ROMs para o console: {console_name}")

                for cell in console_cells:
                    link = cell.find('a')

                    if link:
                        href = link.get('href')

                        if href.endswith('/'):
                            print(f"Link para pasta: {href}")
                            page = requests.get(href)

                            soup_page = BeautifulSoup(page.text, 'html.parser')
                            tabela = soup_page.find('table', class_='archext')

                            if tabela:
                                links_a = tabela.find_all('a')
                                num_urls = len(links_a)

                                if not os.path.exists(pasta_destino_console):
                                    os.makedirs(pasta_destino_console)

                                for link in links_a:
                                    href = link.get('href')
                                    conteudo = link.text

                                    nome_arquivo_local = os.path.join(pasta_destino_console, conteudo)
                                    download_url = "https:" + href  # Adicione "https:" ao href para formar o URL completo

                                    # Realizar o download
                                    download_file(download_url, nome_arquivo_local)

                                    print(f'Arquivo baixado com sucesso: {nome_arquivo_local}')

                                print(f"ROMs baixadas para o console {console_name}.\n")
                            else:
                                print("Não há links para visualizar.")
                        else:
                            print("Não é uma pasta")
            
    elif resposta_init == "2":
        soup = BeautifulSoup(response.text, 'html.parser')

        lista = soup.find('tbody')

        if lista:
            rows = lista.find_all('tr')
            consoles = []

            for row in rows:
                console_cell = row.find('td', height='17')
                cells = row.find_all('td')

                if console_cell:
                    console_name = console_cell.text.strip()
                    consoles.append((console_name, cells))
            # Exibir as opções disponíveis
            while True:
                for idx, (console_name, _) in enumerate(consoles, start=1):
                    print(f"{idx}. {console_name}")

                # Pedir ao usuário para escolher uma opção
                escolha = input("Escolha o número correspondente ao console desejado: ")

                try:
                    escolha = int(escolha)
                    if 1 <= escolha <= len(consoles):
                        chosen_console_name, chosen_console_cells = consoles[escolha - 1]
                        print(f"Você escolheu o console: {chosen_console_name}")
                        escolha_valida = True
                        pasta_destino_final = os.path.join(pasta_destino, chosen_console_name)
                        total_size_bt = 0
                        porcentagem_desejada = 0
                        for cell in chosen_console_cells:
                            link = cell.find('a')

                            if link:
                                href = link.get('href')

                                if href.endswith('/'):
                                    print(f"Link para pasta: {href} \n")
                                    page = requests.get(href)

                                    soup_page = BeautifulSoup(page.text, 'html.parser')
                                    size_cells = soup_page.find_all('td', {'id': 'size'})

                                    for size_cell in size_cells:
                                        size_bt = int(size_cell.text.strip())
                                        total_size_bt += size_bt
                                    total_size_kb = total_size_bt / 1010
                                    total_size_mb = total_size_kb / 1010  # Convertendo para MB
                                    
                                    opcao_download = input("Deseja baixar todas as roms, ver cada uma delas, escolher outro console ou baixar uma porcentagem dessas roms ?\n1 - Baixar todas as roms\n2 - Ver as roms\n3 - outro console \n4 - porcentagem\nEscolha: ")

                                    if opcao_download == '1':
                                        tabela = soup_page.find('table', class_='archext')
                                        if tabela:
                                            links_a = tabela.find_all('a')
                                            num_urls = len(links_a)
                                            print(f"Foram encontradas {num_urls} ROMs.")

                                            if not os.path.exists(pasta_destino_final):
                                                os.makedirs(pasta_destino_final)

                                            if total_size_mb > 1000:
                                                total_size_gb = total_size_mb / 1024  # Convertendo para GB
                                                print(f"Tamanho total dos arquivos: {total_size_gb:.2f} GB\n")
                                            else:
                                                print(f"Tamanho total dos arquivos: {total_size_mb:.2f} MB\n")
                                            for link in links_a:
                                                href = link.get('href')
                                                conteudo = link.text
                                                print(f"Conteúdo: {conteudo}")

                                                nome_arquivo_local = os.path.join(pasta_destino_final, conteudo)
                                                download_url = "https:" + href  # Adicione "https:" ao href para formar o URL completo

                                                # Realizar o download
                                                download_file(download_url, nome_arquivo_local)

                                                print(f'Arquivo baixado com sucesso: {nome_arquivo_local}')
                                            print("Baixando todas as roms...")

                                    elif opcao_download == '2':
                                        tabela = soup_page.find('table', class_='archext')
                                        if tabela:
                                            links_a = tabela.find_all('a')
                                            num_urls = len(links_a)
                                            for link in links_a:
                                                href = link.text
                                                print(href)
                                            print(f"\nForam encontradas {num_urls} ROMs.")
                                            if total_size_mb > 1000:
                                                total_size_gb = total_size_mb / 1024  # Convertendo para GB
                                                print(f"Tamanho total dos arquivos: {total_size_gb:.2f} GB\n")
                                            else:
                                                print(f"Tamanho total dos arquivos: {total_size_mb:.2f} MB\n")
                                            escolha_dd = input(f"Agora quer baixar todas as roms ? \n1 - Claro \n2 - quero n fi")

                                            if opcao_download == '1':
                                                tabela = soup_page.find('table', class_='archext')
                                                if tabela:
                                                    links_a = tabela.find_all('a')
                                                    if not os.path.exists(pasta_destino_final):
                                                        os.makedirs(pasta_destino_final)
                                                    for link in links_a:
                                                        href = link.get('href')
                                                        conteudo = link.text
                                                        print(f"Href: {href}, conteúdo: {conteudo}")

                                                        nome_arquivo_local = os.path.join(pasta_destino_final, conteudo)
                                                        download_url = "https:" + href  # Adicione "https:" ao href para formar o URL completo

                                                        # Realizar o download
                                                        download_file(download_url, nome_arquivo_local)

                                                        print(f'Arquivo baixado com sucesso: {nome_arquivo_local}')
                                                    print("Baixando todas as roms...")
                                            else:
                                                print("a entao ta bom")
                                        else:
                                            print("Não há links para visualizar.")
                                    elif opcao_download == '3':
                                        break
                                    elif opcao_download == '4':
                                        porcentagem_desejada = float(input(f"Digite a porcentagem que deseja baixar do console: {console_name} \n ="))
                                        porcentagem_baixada = 0
                                        tabela = soup_page.find('table', class_='archext')
                                        if tabela:
                                            links_a = tabela.find_all('a')
                                            if not os.path.exists(pasta_destino_final):
                                                os.makedirs(pasta_destino_final)
                                            
                                            for link in links_a:
                                                href = link.get('href')
                                                conteudo = link.text

                                                nome_arquivo_local = os.path.join(pasta_destino_final, conteudo)
                                                download_url = "https:" + href  # Adicione "https:" ao href para formar o URL completo

                                                # Realizar o download
                                                download_file(download_url, nome_arquivo_local)

                                                print(f'Arquivo baixado com sucesso: {nome_arquivo_local}')

                                                # Atualizando a porcentagem baixada
                                                porcentagem_baixada += (os.path.getsize(nome_arquivo_local) / (1024 * 1024))  # Convertendo para MB
                                                
                                                print(f"Porcentagem baixada: {porcentagem_baixada:.2f}%")

                                                # Verificando se a porcentagem desejada foi atingida
                                                if float(porcentagem_baixada) >= porcentagem_desejada:
                                                    print("Porcentagem desejada atingida. Encerrando o download.")
                                                    break
                                    else:
                                        print("Opção inválida.")
                                else:
                                    print("Não é uma pasta")
                    else:
                        print("Escolha inválida.")
                    resposta_continuar = input("Deseja continuar e baixar de outros consoles ? (s/n)? ").lower()
                    if resposta_continuar != 's':
                        break
                except ValueError:
                    print("Escolha inválida. Insira um número válido.")
        else:
            print("nao foi possivel achar os consoles")
    else:
        print("resposta incorreta, digite novamente mano!!!!")
else:
    print("Falha na solicitação HTTP, verifique sua conexao wifi")