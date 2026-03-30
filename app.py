import json
import os
from datetime import datetime

ARQUIVO_DADOS = 'banco_cantina.json'

# Cardápio inicial com flag de disponibilidade (RF04)
CARDAPIO_INICIAL = {
    "1": {"nome": "Coxinha", "preco": 7.50, "disponivel": True},
    "2": {"nome": "Pão de Queijo", "preco": 5.00, "disponivel": True},
    "3": {"nome": "Refrigerante Lata", "preco": 6.00, "disponivel": True},
    "4": {"nome": "Prato Feito (Almoço)", "preco": 22.00, "disponivel": False} # Faltando hoje
}

def carregar_banco():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    return {"pedidos": [], "cardapio": CARDAPIO_INICIAL}

def salvar_banco(dados):
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados, f, indent=4)
