# AnalytiCode back <img src="/images/Python-logo-notext.svg.png" alt="Python" width="30" height="30">

Este projeto foi gerado em python [Python](https://docs.python.org/pt-br/3/) versão 3.13.0.

## É necessário instalar o python

[Baixar Python](https://www.python.org/downloads/)

## Rodar o AnalytiCode back

* Para rodar é necessário instalar o `python` 
* Intalar o `FastAPI` que é uma biblioteca de integração com IAs 
* Intalar o `uvicorn` que é a documentação para o back.

``` bash
pip install fastapi
```

``` bash
pip install uvicorn
```

## Servidor de desenvolvimento

Execute o comando `uvicorn main:app --reload` para um servidor dev. Navegue até `http://localhost:8000/`.

``` bash
uvicorn main:app --reload
```

## Servidor de deploy

[Acessar o back do bot AnalytiCode](https://bot-ia-back.onrender.com/)
