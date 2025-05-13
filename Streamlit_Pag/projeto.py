# Bibliotecas para exibição dos dados e análises
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import numpy as np
import os

# Configurações iniciais
st.set_page_config(page_title="Dashboard", page_icon="♻️", layout="wide")

# Menu lateral
with st.sidebar:
    seleted = option_menu(
        menu_title="MENU",
        options=["Home", "Limpa Brasil", "Ecopontos", "Pontos Revitalizados", 
                 "Pontos de Entrega Voluntaria", "Sobre"],
        icons=["house", "globe-americas", "flag", "pin", "map", "info-circle"],
        default_index=0
    )

# df_zonas = df.query()
# Função: Tela Limpa Brasil
def limp_br():
    st.title("Instituto Limpa Brasil")
    st.subheader("O Instituto Limpa Brasil foi fundado pela empresa Atitude Brasil em 2010. " \
    "Somos uma organização sem fins lucrativos que atua no Brasil como parceira do movimento global Let’s do It. " \
    "Colaborando localmente para o crescimento de ações de limpeza por um mundo sem lixo, mobilizando pessoas e organizações em defesa do descarte adequado de resíduos.")
    
    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    fig_pizza = px.pie(y, labels = mylabels)
    st.plotly_chart(fig_pizza, use_container_width=True) 


# Função: Tela Ecoponto
def ecoponto():
    # Caminho correto para leitura do arquivo (ajustável conforme local do seu projeto)
    caminho_arquivo = "Dados_Geosampa_Prefeitura/bDADOS_XLSX/SIRGAS_GPKG_ecoponto_SIRGAS_GPKG_ecoponto.xlsx"

    try:
        df = pd.read_excel(caminho_arquivo)

        # Filtros na barra lateral
        empresas = st.sidebar.multiselect(
            "Empresa", 
            options=df["ep_empresa"].unique(),
            default=df["ep_empresa"].unique(),
            key="empresa"
        )

        recebimentos = st.sidebar.multiselect(
            "Tipo de Recebimento", 
            options=df["ep_rec_tip"].unique(),
            default=df["ep_rec_tip"].unique(),
            key="recebimento"
        )

        # Aplicar filtros
        df_selecao = df.query("`ep_empresa` in @empresas and ep_rec_tip in @recebimentos")

        # Agrupar dados
        df_agrupado = df_selecao.groupby("ep_empresa").size().reset_index(name="quantidade")

        # Gráfico
        fig_barras = px.bar(
            df_agrupado, 
            x="ep_empresa",
            y="quantidade", 
            color="ep_empresa",
            barmode="group",
            title="Empresas Responsáveis"
        )

    except FileNotFoundError:
        st.error("Arquivo 'ECOPONTO.xlsx' não encontrado. Verifique o caminho ou mova o arquivo para a pasta correta.")
        st.code(f"Caminho procurado: {caminho_arquivo}")
    
    quant_eco = df["ep_empresa"].count()

    st.title("Ecopontos")
    st.subheader(f"Os ecopontos são locais para entrega voluntária de pequenos volumes, os quais buscam eliminar o descarte irregular na cidade, recebendo também materiais inservíveis. Ao todo, a Prefeitura de São Paulo  tem {quant_eco} ecopontos espalhados por toda capital.")
    
    # Exibir gráfico
    st.plotly_chart(fig_barras, use_container_width=True)

def pontosEntregaVoluntaria():
    caminho_arquivo = 'Dados_Geosampa_Prefeitura/bDADOS_TRATADOS/PONTO DE ENTREGA VOLUNTARIA.xlsx'
    
    try:
        st.title("Pontos de Entrega Voluntária (PEVs) em São Paulo")
        st.subheader("PEVs (Pontos de Entrega Voluntária) são locais disponibilizados pela prefeitura onde os cidadãos podem descartar voluntariamente materiais recicláveis, como papel, plástico, vidro e metal. Esses pontos contribuem para a coleta seletiva, a redução do descarte irregular e a preservação do meio ambiente.")
        df = pd.read_excel(caminho_arquivo)
        
        st.sidebar.header("Filtro por Região")
        
        mapeamento_zonas = {
            'Zona Leste': 'Zona Leste',
            'Zona Norte': 'Zona Norte',
            'Zona Sul': 'Zona Sul',
            'Zona Oeste': 'Zona Oeste',
            'Centro': 'Centro',
            'Zona Sudeste': 'Zona Sul',
            'Zona Noroeste': 'Zona Norte',  
        }
        
        df['região_agrupada'] = df['região'].replace(mapeamento_zonas)
        
        regioes = st.sidebar.multiselect(
            "Selecione as regiões:",
            options=df['região_agrupada'].unique(),
            default=df['região_agrupada'].unique(),
            key="regiao"
        )
        
        df_selecao = df.query("região_agrupada in @regioes")
        
        df_agrupado = df_selecao.groupby('região_agrupada')['pev_quanti'].sum().reset_index()

        fig_barras = px.bar(
            df_agrupado,
            x="região_agrupada",
            y="pev_quanti",
            color="região_agrupada",
            title="Quantidade Total de PEV por Região de São Paulo",
            labels={
                "região_agrupada": "Região",
                "pev_quanti": "Quantidade de PEV"
            },
            text_auto=True
        )

        fig_barras.update_layout(
            xaxis_title="Região de São Paulo",
            yaxis_title="Quantidade Total de PEV",
            showlegend=False,
            height=500
        )
        
        fig_map = px.scatter_map(
                df_selecao,
                lat="latitude",
                lon="longitude",
                size="pev_quanti",
                color="pev_subprf",
                hover_name="pev_nome",
                hover_data={
                    "pev_endere": True,
                    "pev_quanti": True,
                    "latitude": False,
                    "longitude": False
                },
                zoom=10,
                height=600,
                size_max=30,
                color_discrete_sequence=px.colors.qualitative.Set2,
                labels={
                    "pev_subprf": "Subprefeitura",
                    "pev_quanti": "Quantidade de PEV",
                    "pev_nome": "Nome do PEV",
                    "pev_endere": "Endereço"
                },
        )

        fig_map.update_layout(
            mapbox_style="open-street-map",
            mapbox_center={"lat": -23.55, "lon": -46.63},
            margin={"r":0, "t":0, "l":0, "b":0}
        )

        if df_agrupado.empty:
            st.warning("Nenhuma região selecionada ou não há dados para exibir.")
        else:
            st.plotly_chart(fig_barras, use_container_width=True)
            st.plotly_chart(fig_map, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

# Execução da página conforme seleção do menu
if seleted == "Home":
    st.title("Bem-vindo ao Painel")

elif seleted == "Limpa Brasil":
    limp_br()

elif seleted == "Ecopontos":
    ecoponto()

elif seleted == "Pontos Revitalizados":
    st.title("Pontos Revitalizados")

elif seleted == "Pontos de Entrega Voluntaria":
    pontosEntregaVoluntaria()

elif seleted == "Sobre":
    st.title("Sobre este Projeto")
