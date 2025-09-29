from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import classificar_email
from responder import gerar_resposta

app = Flask(__name__)
CORS(app, resources={r"/processar": {"origins": "https://autou-api.rvwtech.com.br"}})

@app.route('/processar', methods=['POST'])
def processar():
    data = request.get_json()
    texto = data.get('texto', '')

    if not texto.strip():
        return jsonify({'erro': 'Texto vazio'}), 400

    categoria = classificar_email(texto)
    resposta = gerar_resposta(texto, categoria)

    return jsonify({
        'categoria': categoria,
        'resposta': resposta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)