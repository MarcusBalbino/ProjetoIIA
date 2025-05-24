# Transformando o OlericolasFrutas.txt em um dataframe e convertendo para um csv
dic_localizacao = {}

with open("localizacao.txt", "r", encoding="utf-8") as file:
    for linha in file.readline():
        nome, coordenadas = linha.split(',')
        dic_localizacao[nome] = coordenadas
print(dic_localizacao)