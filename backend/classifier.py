from transformers import pipeline

def classificar_email(texto):
    classificador = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    resultado = classificador(texto)[0]
    return "Produtivo" if resultado['label'] == 'POSITIVE' else "Improdutivo"
