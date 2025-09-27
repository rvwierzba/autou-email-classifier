def classificar_email(texto):
    # Simples heurística ou chamada à API de IA
    if "reunião" in texto.lower() or "proposta" in texto.lower():
        return "Produtivo"
    return "Improdutivo"