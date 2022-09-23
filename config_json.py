import json

with open('credenciais.json') as arquivo_json:
  config = json.load(arquivo_json)

USER = config.get('USER')
PASSWORD = config.get("PASSWORD")
DATABASE = config.get("DATABASE")
JWT_SECRET_KEY = config.get("JWT_SECRET_KEY")
PORT = "5432"
HOST = "localhost" 