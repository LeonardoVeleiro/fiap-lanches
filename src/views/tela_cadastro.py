import streamlit as st
from auth.cadastro_auth import cadastrar_usuario


def exibir_tela_cadastro():
    st.header("Cadastro de Usuário")

    nome = st.text_input("Nome completo")
    email = st.text_input("E-mail")
    rm = st.text_input("RM")
    senha = st.text_input("Senha", type="password")
    confirmar_senha = st.text_input("Confirmar senha", type="password")

    if st.button("Cadastrar"):
        sucesso, mensagem = cadastrar_usuario(
            nome,
            email,
            rm,
            senha,
            confirmar_senha
        )

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)
