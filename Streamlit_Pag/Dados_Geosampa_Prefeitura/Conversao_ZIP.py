import os
import zipfile

# Nome da subpasta onde estão os arquivos .zip
subpasta = "bDADOS_ZIP"
caminho_pasta = os.path.join(os.getcwd(), subpasta)

# Caminho onde os arquivos serão extraídos
caminho_destino = os.path.join(os.getcwd(), "bDADOS_EXTRAIDOS")
os.makedirs(caminho_destino, exist_ok=True)

# Lista os arquivos .zip e extrai
for nome_arquivo in os.listdir(caminho_pasta):

    if nome_arquivo.endswith('.zip'):
        caminho_zip = os.path.join(caminho_pasta, nome_arquivo)

        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            pasta_extracao = os.path.join(caminho_destino, os.path.splitext(nome_arquivo)[0])
            os.makedirs(pasta_extracao, exist_ok=True)
            zip_ref.extractall(pasta_extracao)
            print(f'Extraído: {nome_arquivo} para {pasta_extracao}')
