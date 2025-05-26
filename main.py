from Processamento import to_csv, calcula_distancia
from EstruturasDeDados import get_alimentos, get_localidades

# Para transformar os dados em "EstruturadeDeDados.py" em csv
"""
to_csv(get_alimentos(), "alimentos")
to_csv(get_localidades(), "localidades")
"""
# Entrando com localização para o cálculo de distância

#loc_usuario = input("Digite as suas coordenas: ")
user_loc = (-15.835670673443701, -47.97667463132274)
distribuidor = input("Digite o ponto de distribuição" \
                    " que você quer encontrar: ")
if distribuidor:
    calcula_distancia(user_loc, distribuidor)
else:
    calcula_distancia(user_loc)