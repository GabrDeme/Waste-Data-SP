# Bibliotecas para exibição dos dados e análises
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
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

# Função: Tela Limpa Brasil
def limp_br():
    st.title("Instituto Limpa Brasil")
    st.subheader("O Instituto Limpa Brasil foi fundado pela empresa Atitude Brasil em 2010. " \
    "Somos uma organização sem fins lucrativos que atua no Brasil como parceira do movimento global Let’s do It. " \
    "Colaborando localmente para o crescimento de ações de limpeza por um mundo sem lixo, mobilizando pessoas e organizações em defesa do descarte adequado de resíduos.")

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
    st.title("Pontos de Entrega Voluntária")

elif seleted == "Sobre":
    st.title("Sobre este Projeto")
