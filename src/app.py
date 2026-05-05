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

st.html("""
<div style="display:flex; align-items:center; justify-content:center; gap:15px; margin-bottom:10px;">
    <div style="
        width:80px;
        height:80px;
        background-color:#ED145B;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;
        font-weight:Light;
        border-radius:8px;
        font-size:80px;
        font-family:Arial;
    ">
        F
    </div>

    <div>
        <h2 style="margin:0; letter-spacing:1px; color:white; font-family: Arial; font-size:40px;">
            FIAP Lanches
        </h2>
    </div>
</div>
""")

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
        exibir_tela_cliente()

    elif usuario_logado["perfil"] == "gerente":
        exibir_tela_gerente(
            carregar_pedidos,
            salvar_pedidos,
            carregar_cardapio,
            salvar_cardapio
        )