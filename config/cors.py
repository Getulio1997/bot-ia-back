from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://analyticode.onrender.com", "http://localhost:4200"],
        allow_credentials=True,
        allow_methods=["POST"],  
        allow_headers=["*"],  
    )