import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# URL do site (substitua pela URL real)
url = "https://capital.sp.gov.br/w/conhe%C3%A7a-os-ecopontos-da-cidade-de-s%C3%A3o-paulo"

# Requisição
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Lista para armazenar os dados extraídos
dados_ecopontos = []

# Encontrar os blocos (ajuste o seletor com base na estrutura do site real)
blocos = soup.find_all("p")

for bloco in blocos:
    texto = bloco.get_text(separator="\n")

    # Extrair com regex
    ecoponto = re.search(r"Ecoponto:\s*(.+)", texto)
    endereco = re.search(r"Endereço:\s*(.+)", texto)
    cep = re.search(r"CEP:\s*([\d\-]+)", texto)
    observacao = re.search(r"\*\s*(.+)", texto)

    if ecoponto and endereco and cep:
        dados_ecopontos.append({
            "Ecoponto": ecoponto.group(1),
            "Endereço": endereco.group(1),
            "CEP": cep.group(1),
            "Observação": observacao.group(1) if observacao else ""
        })

# Criar DataFrame
df = pd.DataFrame(dados_ecopontos)

# Exibir ou salvar
print(df)
