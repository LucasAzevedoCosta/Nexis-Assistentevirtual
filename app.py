from flask import Flask,render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

app = Flask(__name__)
app.secret_key = 'alura'

@app.route("/chat", methods=["post"])

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
