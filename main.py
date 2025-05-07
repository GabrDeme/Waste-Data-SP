# Importando bibliotecas
import pandas as pd

# Importando arquivos para dentro do programa

#try:
if True:
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

#except Exception as e:
#    print(e)

df2013 = pd.DataFrame(ano2013)
print(df2013)
df2014 = pd.DataFrame(ano2014)
df2015 = pd.DataFrame(ano2015)
df2016 = pd.DataFrame(ano2016)
df2017 = pd.DataFrame(ano2017)
df2018 = pd.DataFrame(ano2018)
df2019 = pd.DataFrame(ano2019)
df2020 = pd.DataFrame(ano2020)
df2021 = pd.DataFrame(ano2021)
df2022 = pd.DataFrame(ano2022)
df2023 = pd.DataFrame(ano2023)
df2024 = pd.DataFrame(ano2024)

