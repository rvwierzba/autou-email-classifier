from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from classifier import classificar_email
from responder import gerar_resposta
import os

# Caminho absoluto para a pasta frontend
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')
CORS(app, resources={r"/processar": {"origins": "https://autou-api.rvwtech.com.br"}})

# Serve index.html na raiz
@app.route('/')
def index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

# Serve arquivos estáticos (CSS, JS, etc.)
@app.route('/<path:path>')
def static_files(path):
    file_path = os.path.join(FRONTEND_FOLDER, path)
    if os.path.exists(file_path):
        return send_from_directory(FRONTEND_FOLDER, path)
    else:
        return "Arquivo não encontrado", 404

# Rota de processamento
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