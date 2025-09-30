from transformers import pipeline

def gerar_resposta(texto, categoria):
    prompt = f"Escreva uma resposta educada para o seguinte e-mail:\n\n{texto}\n\nCategoria: {categoria}"

    gerador = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        tokenizer="google/flan-t5-small",
        device=-1  # usa CPU
    )

    resultado = gerador(
        prompt,
        max_new_tokens=128,
        do_sample=False
    )

    resposta = resultado[0]['generated_text'].strip()
    return resposta