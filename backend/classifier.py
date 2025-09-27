from transformers import pipeline

# Carrega pipeline de classificação de texto
classificador = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classificar_email(texto):
    resultado = classificador(texto)[0]
    if resultado['label'] == 'POSITIVE':
        return "Produtivo"
    else:
        return "Improdutivo"