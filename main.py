from Processamento import to_csv
from EstruturasDeDados import get_alimentos, get_localidades

# Para transformar os dados em "EstruturadeDeDados.py" em csv
to_csv(get_alimentos(), "alimentos")
to_csv(get_localidades(), "localidades")