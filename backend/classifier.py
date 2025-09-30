def classificar_email(texto):
    texto = texto.lower()

    if "reunião" in texto or "encontro" in texto or "agenda" in texto:
        return "Agendamento"
    elif "orçamento" in texto or "preço" in texto or "pagamento" in texto:
        return "Financeiro"
    elif "problema" in texto or "erro" in texto or "suporte" in texto or "falha" in texto:
        return "Suporte Técnico"
    elif "contrato" in texto or "documento" in texto or "jurídico" in texto:
        return "Jurídico"
    elif "projeto" in texto or "planejamento" in texto:
        return "Gestão de Projetos"
    else:
        return "Outros"