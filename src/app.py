import streamlit as st

from services.banco_service import carregar_json, salvar_json


ARQUIVO_CARDAPIO = "src/data/cardapio.json"
ARQUIVO_PEDIDOS = "src/data/pedidos.json"


def carregar_cardapio():
    return carregar_json(ARQUIVO_CARDAPIO, [])


def carregar_pedidos():
    return carregar_json(ARQUIVO_PEDIDOS, [])


def salvar_cardapio(cardapio):
    salvar_json(ARQUIVO_CARDAPIO, cardapio)


def salvar_pedidos(pedidos):
    salvar_json(ARQUIVO_PEDIDOS, pedidos)


st.set_page_config(
    page_title="FIAP Lanches",
    layout="wide"
)

st.title("FIAP Lanches")
st.info("Estrutura inicial criada. Módulos de login, cliente e gerente serão adicionados nas próximas etapas.")