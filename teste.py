import requests
from bs4 import BeautifulSoup

url = "https://archive.org/details/ni-romsets"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    lista = soup.find('tbody')

    if lista:
        rows = lista.find_all('tr')
        total_size_bt = 0

        for row in rows:
            cells = row.find_all('td')

            for cell in cells:
                link = cell.find('a')
                size_cell = cell.find('td', {'id': 'size'})

                if link and size_cell:
                    href = link.get('href')
                    size_bt = int(size_cell.text.strip())
                    total_size_bt += size_bt

                    if href.endswith('/'):
                        page = requests.get(href)
                        soup_page = BeautifulSoup(page.text, 'html.parser')
                        size_cells = soup_page.find_all('td', {'id': 'size'})

                        for size_cell in size_cells:
                            size_bt = int(size_cell.text.strip())
                            total_size_bt += size_bt

        total_size_kb = total_size_bt / 1024
        total_size_mb = total_size_kb / 1024
        total_size_gb = total_size_mb / 1024

        print(f"Tamanho total das ROMs a serem baixadas: {total_size_gb:.2f} GB")

    else:
        print("Não foi possível encontrar a lista de consoles.")
else:
    print("Falha na solicitação HTTP.")
