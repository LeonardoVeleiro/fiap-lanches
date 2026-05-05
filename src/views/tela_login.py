import streamlit as st
from auth.login_auth import login_usuario


def exibir_tela_login():
    st.header("Login")

    rm = st.text_input("RM")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        sucesso, resultado = login_usuario(rm, senha)

        if sucesso:
            st.session_state["logado"] = True
            st.session_state["usuario"] = resultado
            st.success(f"Bem-vindo(a), {resultado['nome']}!")
            st.rerun()
        else:
            st.error(resultado)
