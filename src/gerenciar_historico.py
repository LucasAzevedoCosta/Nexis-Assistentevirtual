import google.generativeai as genai

MODELO_ESCOLHIDO = "gemini-1.5-flash"   

def resumir_historico(historico):
    """
    Resumir o histórico de mensagens para manter a relevância e a coerência.
    Este método é chamado quando o histórico atinge 10 mensagens.
    """
    # Unindo as partes do histórico em um único texto para sumarização
    texto_completo = " ".join([
        parte.text if hasattr(parte, 'text') else parte
        for mensagem in historico for parte in mensagem['parts']
    ])

    # Criando o prompt para resumir o histórico
    prompt_resumo = f"""
    Resuma o seguinte histórico mantendo as informações essenciais para continuar uma conversa coerente:
    {texto_completo}
    """

    # Configurando o modelo para gerar o resumo
    llm = genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction="Você é um assistente de resumo.",
        generation_config={"temperature": 0.5, "max_output_tokens": 512}
    )

    # Gerando o resumo do histórico
    resposta = llm.generate_content(prompt_resumo)
    resumo = resposta.text.strip()

    # Criando uma nova entrada de resumo no histórico
    historico_resumido = [{'role': 'model', 'parts': [resumo]}]

    return historico_resumido