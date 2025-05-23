# Transformando o OlericolasFrutas.txt em um dataframe e convertendo para um csv

with open("OlericolasFrutas.txt", "r", encoding="utf-8") as file:
    for linha in file:
        print(f'{linha.strip()}')