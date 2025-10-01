from transformers import pipeline

# Carrega o modelo leve uma única vez
gerador = pipeline(
    "text2text-generation",
    model="google/flan-t5-xs",
    tokenizer="google/flan-t5-xs",
    device=-1  # força uso de CPU
)

def gerar_resposta(texto, categoria):
    prompt = f"Escreva uma resposta educada para o seguinte e-mail:\n\n{texto}\n\nCategoria: {categoria}"

    resultado = gerador(
        prompt,
        max_new_tokens=64,
        do_sample=False
    )

    resposta = resultado[0]['generated_text'].strip()
    return resposta