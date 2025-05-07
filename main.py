# Importando bibliotecas
import pandas as pd

# Dicionario vazio
tabelao = {}
dfTabelao = pd.DataFrame(tabelao)
# Importando arquivos para dentro do programa

try:
    ano2013 = pd.read_csv("baseDados/coletaLixoSP_2013.csv", sep=';')
    ano2014 = pd.read_csv("baseDados/coletaLixoSP_2014.csv", sep=';')
    ano2015 = pd.read_csv("baseDados/coletaLixoSP_2015.csv", sep=';')
    ano2016 = pd.read_csv("baseDados/coletaLixoSP_2016.csv", sep=';')
    ano2017 = pd.read_csv("baseDados/coletaLixoSP_2017.csv", sep=';')
    ano2018 = pd.read_csv("baseDados/coletaLixoSP_2018.csv", sep=';')
    ano2019 = pd.read_csv("baseDados/coletaLixoSP_2019.csv", sep=';')
    ano2020 = pd.read_csv("baseDados/coletaLixoSP_2020.csv", sep=';')
    ano2021 = pd.read_csv("baseDados/coletaLixoSP_2021.csv", sep=';')
    ano2022 = pd.read_csv("baseDados/coletaLixoSP_2022.csv", sep=';')
    ano2023 = pd.read_csv("baseDados/coletaLixoSP_2023.csv", sep=';')
    ano2024 = pd.read_csv("baseDados/coletaLixoSP_2024.csv", sep=';')

except Exception as e:
    print(e)

df2013 = pd.DataFrame(ano2013)
coluna2013 = df2013.iloc[20]
dfTabelao["2013"] = pd.DataFrame(coluna2013)

df2014 = pd.DataFrame(ano2014)
coluna2014 = df2014.iloc[19]
dfTabelao["2014"] = pd.DataFrame(coluna2014)

df2015 = pd.DataFrame(ano2015)
coluna2015 = df2015.iloc[21]
dfTabelao["2015"] = pd.DataFrame(coluna2015)

df2016 = pd.DataFrame(ano2016)
coluna2016 = df2016.iloc[24]
dfTabelao["2016"] = pd.DataFrame(coluna2016)

df2017 = pd.DataFrame(ano2017)
coluna2017 = df2017.iloc[22]
dfTabelao["2017"] = pd.DataFrame(coluna2017)

df2018 = pd.DataFrame(ano2018)
coluna2018 = df2018.iloc[22]
dfTabelao["2018"] = pd.DataFrame(coluna2018)

df2019 = pd.DataFrame(ano2019)
coluna2019 = df2019.iloc[29]
dfTabelao["2019"] = pd.DataFrame(coluna2019)

df2020 = pd.DataFrame(ano2020)
coluna2020 = df2020.iloc[33]
dfTabelao["2020"] = pd.DataFrame(coluna2020)

df2021 = pd.DataFrame(ano2021)
coluna2021 = df2021.iloc[33]
dfTabelao["2021"] = pd.DataFrame(coluna2021)

df2022 = pd.DataFrame(ano2022)
coluna2022 = df2022.iloc[33]
dfTabelao["2022"] = pd.DataFrame(coluna2022)

df2023 = pd.DataFrame(ano2023)
coluna2023 = df2023.iloc[33]
dfTabelao["2023"] = pd.DataFrame(coluna2023)

df2024 = pd.DataFrame(ano2024)
coluna2024 = df2024.iloc[33]
dfTabelao["2024"] = pd.DataFrame(coluna2024)

