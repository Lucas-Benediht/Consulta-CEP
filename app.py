from flask import Flask, request, render_template, jsonify
import requests

app = Flask (__name__)

# Rota API
@app.route('/take_cep', methods=['GET'])
def take_cep():
    # Obtém o CEP da consulta a partir dos parâmetros da URL
    cep = request.args.get('cep')
    
    # URL de requisição
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "CEP não encontrado"}), 404
    
# Rota front
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
