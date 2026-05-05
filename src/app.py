import streamlit as st

from services.banco_service import carregar_json, salvar_json
from views.tela_login import exibir_tela_login
from views.tela_cadastro import exibir_tela_cadastro
from views.tela_cliente import exibir_tela_cliente

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

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

if "carrinho" not in st.session_state:
   st.session_state["carrinho"] = {}


if not st.session_state["logado"]:
    menu = st.sidebar.radio("Menu", ["Login", "Cadastro"])
    if menu == "Login":
        exibir_tela_login()
    elif menu == "Cadastro":
        exibir_tela_cadastro()
else:
   usuario_logado = st.session_state["usuario"]

   st.sidebar.success(f"Logado como: {usuario_logado['nome']}")
   st.sidebar.write(f"Perfil: {usuario_logado['perfil']}")

    if st.sidebar.button("Sair"):
       st.session_state["logado"] = False
       st.session_state["usuario"] = None
       st.session_state["carrinho"] = {}
       st.rerun()

   if usuario_logado["perfil"] == "cliente":
       exibir_tela_cliente(
           carregar_cardapio,
           carregar_pedidos,
           salvar_pedidos
       )
   else:
       st.info("Painel do gerente será implementado na próxima etapa.")

