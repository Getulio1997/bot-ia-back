from fastapi import FastAPI, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import RedirectResponse
from back.controller.chatbot import enviar_mensagem
from back.model.mensagem import Mensagem
from config.cors import add_cors
import re

app = FastAPI()

add_cors(app)

def validar_mensagem(mensagem: str) -> bool:
    padroes_codigo = re.compile(r'(\bclass\b|\bfunction\b|\bif\b|\belse\b|\bfor\b|\bwhile\b|\bdo\b|\breturn\b|\bimport\b|\bexport\b|\bnew\b|\bthis\b|\btry\b|\bcatch\b|\bthrow\b|\bfinally\b|\bconst\b|\blet\b|\bvar\b|<\/?[a-z][^>]*>|[{[\]}();]|=>|\bconsole\.log\b|\btypeof\b|\binstanceof\b|\bnull\b|\bundefined\b|\bimport\b|\bexport\b|\btry\b|\bcatch\b|\bthrow\b)', re.IGNORECASE)
    termos_contexto = re.compile(r'\b(código|programação|script|erro|debug)\b', re.IGNORECASE)
    tem_formato_de_codigo = re.compile(r'\b(?:\w+\s*=\s*\w+|function\s*\w+\s*\(|class\s*\w+|[\w\.]+\()', re.IGNORECASE)

    return (padroes_codigo.search(mensagem) or termos_contexto.search(mensagem)) and tem_formato_de_codigo.search(mensagem)

@app.post("/analisa_texto")
def api_analisa_texto(mensagem: Mensagem):
    if not validar_mensagem(mensagem.texto):
        raise HTTPException(status_code=400, detail="A mensagem deve estar relacionada a código.")

    try:
        resposta_modelo = enviar_mensagem(mensagem.texto)
        return {"resposta": resposta_modelo}
    except HTTPException as e:
        raise e

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

class LimitRequestSizeMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_size: int = 200 * 1024 * 1024):
        super().__init__(app)
        self.max_size = max_size

    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > self.max_size:
            raise HTTPException(status_code=413, detail="Payload too large")
        return await call_next(request)

app.add_middleware(LimitRequestSizeMiddleware, max_size=200 * 1024 * 1024)