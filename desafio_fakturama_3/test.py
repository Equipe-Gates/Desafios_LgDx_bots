import json

def carregar_json():
    caminho_arquivo = "C:\\desafios\\desafio_3\\desafio_3\\produtos.json"
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
            
    return dados

load = carregar_json()
produtos = load['load']['products']



for q in produtos:
    print(q)