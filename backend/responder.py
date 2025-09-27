from transformers import pipeline

gerador = pipeline("text-generation", model="gpt2")

def gerar_resposta(texto, categoria):
    prompt = f"Email: {texto}\nCategoria: {categoria}\nResposta:"
    resposta = gerador(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    return resposta.split("Resposta:")[-1].strip()