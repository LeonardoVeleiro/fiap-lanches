import streamlit as st

from views.tela_login import exibir_tela_login
from views.tela_cadastro import exibir_tela_cadastro
from views.tela_cliente import exibir_tela_cliente
from views.tela_gerente import exibir_tela_gerente
from views.tela_estilo import aplicar_estilo

from services.cardapio_service import carregar_cardapio, salvar_cardapio
from services.pedido_service import carregar_pedidos, salvar_pedidos


st.set_page_config(
    page_title="FIAP Lanches",
    layout="wide"
)

aplicar_estilo()

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

    if usuario_logado["perfil"] == "gerente":
        exibir_tela_gerente(
            carregar_pedidos,
            salvar_pedidos,
            carregar_cardapio,
            salvar_cardapio
        )

    else:
        exibir_tela_cliente(
            carregar_cardapio,
            carregar_pedidos,
            salvar_pedidos
        )