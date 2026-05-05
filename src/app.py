import streamlit as st

from views.tela_login import exibir_tela_login
from views.tela_cadastro import exibir_tela_cadastro
from views.tela_cliente import exibir_tela_cliente


st.set_page_config(
    page_title="FIAP Lanches",
    layout="wide"
)


st.title("FIAP Lanches")


# Inicialização do session_state
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = {}


# Usuário não logado
if not st.session_state["logado"]:
    menu = st.sidebar.radio("Menu", ["Login", "Cadastro"])

    if menu == "Login":
        exibir_tela_login()

    elif menu == "Cadastro":
        exibir_tela_cadastro()


# Usuário logado
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
        exibir_tela_cliente()

    elif usuario_logado["perfil"] == "gerente":
        st.info("Painel do gerente será implementado na próxima etapa.")