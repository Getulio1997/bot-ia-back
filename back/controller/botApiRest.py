from fastapi import FastAPI, HTTPException
from back.controller.chatbot import enviar_mensagem
from back.model.mensagem import Mensagem
from config.cors import add_cors

app = FastAPI()

add_cors(app)

@app.post("/analisa_texto")
def api_analisa_texto(mensagem: Mensagem):
    try:
        resposta_modelo = enviar_mensagem(mensagem.texto)
        return {"resposta": resposta_modelo}
    except HTTPException as e:
        raise e