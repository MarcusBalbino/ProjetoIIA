import processamento
import estruturadedados
import requests
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS


# Para transformar os dados em "EstruturadeDeDados.py" em .csv
"""
to_csv(get_alimentos(), "alimentos")
to_csv(get_localidades(), "localidades")
"""
# Entrando com localização para o cálculo de distância


"""localizacao_usuario = input("Digite as suas coordenas: ")
distribuidor = input("Digite o ponto de distribuição" \
                    " que você quer encontrar: ")
if localizacao_usuario and distribuidor:
    processamento.calcula_distancia(localizacao_usuario, distribuidor)
elif localizacao_usuario:
    processamento.calcula_distancia(localizacao_usuario)
else:
    break"""

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
CORS(app)


@app.route("/")
def home():
    # return "Servidor Flask funcionando"
    return render_template("index.html")

@app.route("/recomendacoes")
def pagina_recomendacoes():
    return render_template("recomendacoes.html")

import requests

@app.route("/proxy")
def proxy():
    url = "https://dlnk.one/e?id=nol9RNkNdre4&type=1"
    resposta = requests.get(url)
    return resposta.content



if __name__ == "__main__":
    app.run(debug=True)