import requests

def gerar_resposta(texto, categoria):
    prompt = f"Escreva uma resposta educada para o seguinte e-mail:\n\n{texto}\n\nCategoria: {categoria}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "tinyllama", "prompt": prompt}
    )

    return response.json()["response"].strip()