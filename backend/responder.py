from transformers import pipeline, set_seed

def gerar_resposta(texto, categoria):
    # Define o prompt de entrada
    prompt = f"Email: {texto}\nCategoria: {categoria}\nResposta:"

    # Configura o gerador com modelo leve e truncamento explícito
    gerador = pipeline(
        "text-generation",
        model="sshleifer/tiny-gpt2",
        tokenizer="sshleifer/tiny-gpt2",
        device=-1  # força uso de CPU
    )

    # Define semente para geração mais consistente (opcional)
    set_seed(42)

    # Gera resposta com limites mais leves para CPU
    resultado = gerador(
        prompt,
        max_new_tokens=64,
        do_sample=True,
        temperature=0.7,
        pad_token_id=50256  # evita warnings
    )

    # Extrai apenas o trecho gerado após "Resposta:"
    texto_gerado = resultado[0]['generated_text']
    resposta_final = texto_gerado.split("Resposta:")[-1].strip()

    return resposta_final