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
    print("🔔 Requisição recebida em /processar")

    try:
        data = request.get_json(force=True)
        print("📨 Dados recebidos:", data)
    except Exception as e:
        print("❌ Erro ao decodificar JSON:", e)
        return jsonify({'erro': 'JSON inválido'}), 400

    texto = data.get('texto', '')
    if not texto.strip():
        print("⚠️ Texto vazio")
        return jsonify({'erro': 'Texto vazio'}), 400

    print("🔍 Classificando texto...")
    categoria = classificar_email(texto)
    print("✅ Categoria:", categoria)

    print("🧠 Gerando resposta...")
    resposta = gerar_resposta(texto, categoria)
    print("✅ Resposta:", resposta)

    return jsonify({
        'categoria': categoria,
        'resposta': resposta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)