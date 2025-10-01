from flask import Flask, request, jsonify
from classifier import classificar_email

app = Flask(__name__)

@app.route('/')
def home():
    return 'API de classificação ativa!'

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
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)