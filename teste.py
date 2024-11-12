from flask import Flask, jsonify
import requests


app = Flask(__name__)

import requests

# URL da API
url = "https://api.scryfall.com"

# Fazer a requisição GET para a API
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converter a resposta para um dicionário Python
    data = response.json()
    
    # Imprimir o dicionário para ver sua estrutura
    print(data)
else:
    print(f"Erro: Não foi possível acessar a API. Código: {response.status_code}")



app.run(port=5000,host='localhost', debug=True)
