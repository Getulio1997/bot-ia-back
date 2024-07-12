import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
endpointPost = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"
