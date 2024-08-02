from fastapi import FastAPI, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import RedirectResponse
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
