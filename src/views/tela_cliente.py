import streamlit as st
from services.cardapio_service import carregar_cardapio


def exibir_tela_cliente():
    st.title("Área do Cliente")
    st.subheader("Cardápio")

    cardapio = carregar_cardapio()

    if not cardapio:
        st.warning("Nenhum item cadastrado no cardápio.")
        return

    pesquisa = st.text_input(
        "",
        placeholder="Ex: coxinha, pastel, refrigerante..."
    )

    for item in cardapio:
        nome = item["nome"]
        preco = item["preco"]
        disponivel = item["disponivel"]

        if pesquisa.lower() in nome.lower():
            st.write(f"**{nome}** - R$ {preco:.2f}")

            if disponivel:
                st.success("Disponível")
            else:
                st.error("Indisponível")