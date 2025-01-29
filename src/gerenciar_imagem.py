import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

def gerear_imagem_gemini(caminho_imagem):
    arquivo_temporario = genai.upload_file(
        path=caminho_imagem,
        display_name="Imagem Enviada"
    )

    print(f"imagem enviada: {arquivo_temporario.uri}")
    return arquivo_temporario