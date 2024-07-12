from fastapi import HTTPException
import requests
import json
from api.senhaApi import API_KEY, endpointPost, id_modelo

def enviar_mensagem(pergunta):
    body = {
        "model": id_modelo,
        "messages": [
            {
                "role": "user",
                "content": pergunta
            }
        ]
    }

    body = json.dumps(body)
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    requisicao = requests.post(endpointPost, headers=headers, data=body)
    
    print("Status Code:", requisicao.status_code)
    print("Response Text:", requisicao.text)
    
    if requisicao.status_code == 500:
        raise HTTPException(status_code=500, detail="Erro de servidor!")
    if requisicao.status_code != 200:
        raise HTTPException(status_code=requisicao.status_code, detail=requisicao.text)
    
    resposta = requisicao.json()
    mensagem_resposta = resposta["choices"][0]["message"]["content"]
    return mensagem_resposta
