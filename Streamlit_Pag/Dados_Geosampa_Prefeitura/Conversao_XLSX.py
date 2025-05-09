import os
import pandas as pd
import geopandas as gpd
import fiona

# Pastas
pasta_origem = os.path.join(os.getcwd(), 'bDADOS_EXTRAIDOS')
pasta_destino = os.path.join(os.getcwd(), 'bDADOS_XLSX')
os.makedirs(pasta_destino, exist_ok=True)

# Percorre os arquivos
for raiz, dirs, arquivos in os.walk(pasta_origem):
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(raiz, arquivo)
        nome_base = os.path.splitext(arquivo)[0]
        caminho_xlsx = os.path.join(pasta_destino, f'{nome_base}.xlsx')

        try:
            if arquivo.endswith(('.csv', '.txt')):
                try:
                    # Tenta primeiro com UTF-8
                    df = pd.read_csv(caminho_arquivo, sep=None, engine='python')
                except UnicodeDecodeError:
                    # Se der erro, tenta com latin1
                    df = pd.read_csv(caminho_arquivo, sep=None, engine='python', encoding='latin1')
                df.to_excel(caminho_xlsx, index=False)
                print(f'Convertido CSV/TXT: {arquivo}')
            
            elif arquivo.endswith('.gpkg'):
                camadas = fiona.listlayers(caminho_arquivo)
                for camada in camadas:
                    gdf = gpd.read_file(caminho_arquivo, layer=camada)
                    caminho_xlsx_camada = os.path.join(
                        pasta_destino, f'{nome_base}_{camada}.xlsx'
                    )
                    gdf.to_excel(caminho_xlsx_camada, index=False)
                    print(f'Convertido GPKG: {arquivo} | camada: {camada}')
        
        except Exception as e:
            print(f'Erro ao converter {arquivo}: {e}')
