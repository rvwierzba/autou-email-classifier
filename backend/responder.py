from transformers import pipeline

def gerar_resposta(texto, categoria):
    gerador = pipeline("text-generation", model="sshleifer/tiny-gpt2")
    prompt = f"Email: {texto}\nCategoria: {categoria}\nResposta:"
    resposta = gerador(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    return resposta.split("Resposta:")[-1].strip()
