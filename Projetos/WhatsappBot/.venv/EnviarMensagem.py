import requests
from dotenv import load_dotenv
import os

load_dotenv()

id_instance = os.getenv("ID_INSTANCE")
api_token = os.getenv("API_TOKEN")
url = f"https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{api_token}"

number = os.getenv("CHATID")
message = "Olá, isso é um teste do meu bot com a Green API"

def env_mensagem(msg, img):
    payload = {
        "chatId": number,
        "urlFile": img,
        "fileName": "noticia.jpg",
        "caption": msg
    }
    response = requests.post(url, json=payload)

    # Verificador
    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print("Erro ao enviar mensagem:")
        print(response.status_code, response.text)
