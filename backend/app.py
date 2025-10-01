from flask import Flask, request, jsonify, send_from_directory
import os
from classifier import classificar_email

# Caminho absoluto para a pasta frontend
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(__name__, static_folder=FRONTEND_DIR)

@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route('/processar', methods=['POST'])
def processar():
    try:
        dados = request.get_json(force=True)
        texto = dados.get('texto', '').strip()

        if not texto:
            return jsonify({'erro': 'Texto vazio ou ausente'}), 400

        categoria = classificar_email(texto)

        return jsonify({
            'categoria': categoria,
            'resposta': f"Este e-mail foi classificado como: {categoria}"
        })

    except Exception as e:
        print(f"❌ Erro interno: {e}")
        return jsonify({'erro': 'Erro interno no servidor'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)