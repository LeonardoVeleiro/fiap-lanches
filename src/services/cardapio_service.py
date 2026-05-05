from services.banco_service import carregar_json, salvar_json

ARQUIVO_CARDAPIO = "src/data/cardapio.json"


def carregar_cardapio():
    return carregar_json(ARQUIVO_CARDAPIO, [])


def salvar_cardapio(cardapio):
    salvar_json(ARQUIVO_CARDAPIO, cardapio)