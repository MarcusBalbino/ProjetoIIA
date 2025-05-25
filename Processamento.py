import pandas as pd
from EstruturasDeDados import get_alimentos, get_localidades

def to_csv(dados):
    df = pd.DataFrame(dados) # - Um DataFrame é uma estrutura de tabela usada para manipular e organizar dados.
    df.to_csv("localidades", encoding='utf-8') # - CSV é um tipo de arquivo que separa os valores por vírgula COMMA Separeted Value
    print("Arquivo localidades criado!")


if __name__=="__main__":
    to_csv()