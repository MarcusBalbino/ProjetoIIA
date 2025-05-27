from processamento import calcula_distancia
from estruturadedados import get_alimentos, get_localidades
from flask import Flask, render_template, jsonify, request


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
    elif localizacao_usuario:
        calcula_distancia(localizacao_usuario)
    else:
        break

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Interface do usuário

@app.route("/dados")
def dados():
    produtores = processamento.carregar_dados().to_dict(orient="records")  # Chamando função do processamento
    return jsonify(produtores)

@app.route("/recomendacoes")
def recomendacoes():
    user_lat = float(request.args.get("lat"))
    user_lon = float(request.args.get("lon"))
    distancia_max = float(request.args.get("distancia"))

    recomendados = processamento.recomendar_produtores(user_lat, user_lon, distancia_max)
    return jsonify(recomendados)

if __name__ == "__main__":
    app.run(debug=True)