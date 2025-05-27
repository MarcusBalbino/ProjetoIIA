from Processamento import to_csv, calcula_distancia
from EstruturasDeDados import get_alimentos, get_localidades

# Para transformar os dados em "EstruturadeDeDados.py" em .csv
"""
to_csv(get_alimentos(), "alimentos")
to_csv(get_localidades(), "localidades")
"""
# Entrando com localização para o cálculo de distância

while True:
    localizacao_usuario = input("Digite as suas coordenas: ")
    distribuidor = input("Digite o ponto de distribuição" \
                        " que você quer encontrar: ")
    if localizacao_usuario and distribuidor:
        calcula_distancia(localizacao_usuario, distribuidor)
    elif:
        calcula_distancia(localizacao_usuario)