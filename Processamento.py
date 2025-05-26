import pandas as pd
import ast
from geopy.distance import geodesic
from EstruturasDeDados import get_alimentos, get_localidades

# Transformando a estrutura de dados em arquivo .csv

def to_csv(dados, nome_arquivo):
    df = pd.DataFrame(dados) # - Um DataFrame é uma estrutura de tabela usada para manipular e organizar dados.
    df_transposto = df.T # Aqui estou transpondo as linhas pelas as colunas.
    df_transposto.to_csv(f'{nome_arquivo}.csv', encoding='utf-8') # - CSV é um tipo de arquivo que separa os valores por vírgula COMMA Separeted Value
    print(f'O arquivo {nome_arquivo}.csv foi criado')


# Processamento de distância

def calcula_distancia(usuario, distribuidora=None):
    df_localidades = pd.read_csv("localidades.csv", index_col=0)
    if distribuidora:
        distancia = geodesic(usuario, distribuidora).km
        print(f'A sua distancia para a {distribuidora}'/
               f'é de {distancia} kilometros.')
    else:
        print("Aqui está a sua distância para" \
        " todas nossas distribuidoras:")
        for sigla, linha in df_localidades.iterrows():
            distancia = geodesic(usuario, 
                        ast.literal_eval(linha["coordenadas"])).km
            print(f'\t{sigla}: {distancia}')

            

# Visual
"""
for index, linha in pd.read_csv("localidades.csv", index_col=0).iterrows():
    distancia = linha["coordenadas"]
    print(distancia)"""
