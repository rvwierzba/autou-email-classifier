from flask import Flask, request, jsonify
from responder import gerar_resposta
from classifier import classificar_email

app = Flask(__name__)

@app.route('/processar', methods=['POST'])
def processar_email():
    dados = request.get_json()
    texto = dados.get('texto', '')

    categoria = classificar_email(texto)
    resposta = gerar_resposta(texto, categoria)

    return jsonify({
        'categoria': categoria,
        'resposta': resposta
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)