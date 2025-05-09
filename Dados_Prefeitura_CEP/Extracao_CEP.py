# Importa as bibliotecas necessárias

import pdfplumber  # Para ler o conteúdo do PDF
import pandas as pd
import requests 

# Função para baixar o PDF de uma URL e salvar localmente
def baixar_pdf(url):
    resposta = requests.get(url)  # Faz o download do PDF
    with open("temp.pdf", "wb") as f:  # Salva como 'temp.pdf'
        f.write(resposta.content)

# Função para extrair tabelas do PDF usando pdfplumber
def extrair_tabelas_pdf(caminho_pdf):
    tabelas = []  # Lista para armazenar todas as tabelas encontradas
    with pdfplumber.open(caminho_pdf) as pdf:  # Abre o PDF
        for page in pdf.pages:  # Percorre cada página
            table = page.extract_table()  # Tenta extrair tabela da página
            if table:  # Se houver tabela na página

                # Cria um DataFrame (a primeira linha vira o nome das colunas)
                df = pd.DataFrame(table[1:], columns=table[0])
                tabelas.append(df)  # Adiciona a tabela à lista

    # Combina todas as tabelas extraídas em um único DataFrame
    return pd.concat(tabelas, ignore_index=True) if tabelas else pd.DataFrame()

# Função para salvar o DataFrame final em um arquivo Excel
def salvar_em_excel(dataframe, nome_arquivo):
    dataframe.to_excel(nome_arquivo, index=False)  # Salva como Excel, sem o índice do DataFrame
    print(f"Tabela salva como '{nome_arquivo}'.")  # Mensagem de sucesso

# URL do PDF (fonte oficial da Prefeitura de São Paulo)
url = "https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/direitos_humanos/participacao_social/CONSELHOS/CONSELHO_IDOSO/ELEICAO/2023/Tabela%20CEP%20(1).pdf"

# Chama as funções em sequência
baixar_pdf(url) 
df = extrair_tabelas_pdf("temp.pdf")
salvar_em_excel(df, "tabela_extraida_prefeitura.xlsx")
