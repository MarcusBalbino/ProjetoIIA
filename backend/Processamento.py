import pandas as pd
import ast
from geopy.distance import geodesic
import estruturadedados

# Transformando a estrutura de dados em arquivo .csv

def to_csv(dados, nome_arquivo):
    df = pd.DataFrame(dados).T # - Um DataFrame é uma estrutura de tabela usada para manipular e organizar dados.
    df.to_csv(f'{nome_arquivo}.csv', encoding='utf-8') # - CSV é um tipo de arquivo que separa os valores por vírgula COMMA Separeted Values
    #print(f'O arquivo {nome_arquivo}.csv foi criado')


# Processamento de distância

def calcula_distancia(usuario, distribuidora):
    distancia = geodesic(usuario, distribuidora).km # A distancia do usuário para o distribuidor
    return distancia

"""    else:
        for sigla, linha in df_localidades.iterrows():
            distancia = geodesic(usuario, 
                        ast.literal_eval(linha["coordenadas"])).km # A distância do usuário para todos os distribuidores
            lista_distancia.append(distancia)"""
# Leitura do arquivo csv

def carregar_dados():
    return pd.read_csv("backend/localidades.csv")

# 

def recomendar_produtores(coordenadas_usr, max_distancia):
    df_localidades = carregar_dados()
    distribuidoras_recomendadas = []
    for sigla, linha in df_localidades.iterrows():
        if max_distancia >= calcula_distancia(coordenadas_usr,
                                    ast.literal_eval(linha["coordenadas"])):
            distribuidoras_recomendadas.append()
    

# Visual

"""for index, linha in pd.read_csv("backend/localidades.csv", index_col=0).iterrows():
    distancia = linha
    print(distancia)"""
