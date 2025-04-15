import requests
from dotenv import load_dotenv
import os

load_dotenv()

id_instance = os.getenv('ID_INSTANCE')
api_token = os.getenv('API_TOKEN')

if not id_instance or not api_token:
    raise ValueError("Erro nas variáveis de ambiente")

url = f'https://api.green-api.com/waInstance{id_instance}/GetChats/{api_token}'

response = requests.get(url)

if response.status_code == 200:
    chats = response.json()
    for chat in chats:
        # Ignora grupos
        if not chat['id'].endswith('@g.us'):
            nome = chat.get('name', 'Sem nome')
            print(f"Usuário: {nome} - ID: {chat['id']}")
else:
    print("Erro ao buscar chats:", response.text)