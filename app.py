from flask import Flask,render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
from time import sleep
from helper import carrega, salva
from selecionar_persona import personas

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

app = Flask(__name__)
app.secret_key = 'alura'

contexto = carrega("dados/musimart.txt")

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            personalidade = personas[""]

            prompt_do_sistema = f"""
            # PERSONA

            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
 
            Você deve usar apenas dados utilizar apenas dados que estajam dentro do 'contexto'

            # CONTEXTO
            {contexto}

            # PERSONALIDADE
            {personalidade}
            """

            configuracao_modelo = {
                "temperature" : 0.1,
                "max_output_tokens" : 8192
            }

            llm = genai.GenerativeModel(
                model_name=MODELO_ESCOLHIDO,
                system_instruction=prompt_do_sistema,
                generation_config=configuracao_modelo
            )

            resposta = llm.generate_content(prompt)
            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro

            sleep(50)

@app.route("/chat", methods=["post"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
