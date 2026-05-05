import streamlit as st

from services.gerente_service import (
    listar_pedidos_na_fila,
    marcar_pedido_como_pronto,
    atualizar_preco_produto,
    alterar_disponibilidade_produto,
    cadastrar_produto
)

def exibir_tela_gerente(
    carregar_pedidos,
    salvar_pedidos,
    carregar_cardapio,
    salvar_cardapio
):
    st.header("Painel do Gerente")

    aba1, aba2, aba3 = st.tabs([
        "Fila de Pedidos",
        "Controle do Cardápio",
        "Cadastrar Produto"
    ])

    with aba1:
        pedidos = carregar_pedidos()
        pedidos_na_fila = listar_pedidos_na_fila(pedidos)

        if not pedidos_na_fila:
            st.info("Nenhum pedido no momento.")
        else:
            for pedido in pedidos_na_fila:
                with st.container(border=True):
                    st.write(f"### Pedido #{pedido.get('id', '-')}")
                    st.write(f"**Cliente:** {pedido['usuario']}")
                    st.write(f"**Status:** {pedido['status']}")
                    st.write(f"**Total:** R$ {pedido['total']:.2f}")

                    st.write("**Itens:**")
                    for item in pedido["itens"]:
                        quantidade = item.get("quantidade", 1)
                        st.write(
                            f"- {item['nome']} | Qtd: {quantidade} | R$ {item['preco']:.2f}"
                        )

                    if st.button("✓", key=f"pronto_{pedido['id']}"):
                        sucesso, mensagem = marcar_pedido_como_pronto(
                            pedidos,
                            pedido["id"]
                        )

                        if sucesso:
                            salvar_pedidos(pedidos)
                            st.success(mensagem)
                            st.rerun()
                        else:
                            st.error(mensagem)

    with aba2:
        cardapio = carregar_cardapio()

        for item in cardapio:
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns([3, 2, 2, 2])

                with col1:
                    st.write(f"**{item['nome']}**")
                    st.write(f"Preço atual: R$ {item['preco']:.2f}")

                with col2:
                    if item["disponivel"]:
                        st.success("Disponível")
                    else:
                        st.error("Indisponível")

                with col3:
                    novo_preco = st.number_input(
                        "Novo preço",
                        min_value=0.0,
                        value=float(item["preco"]),
                        step=0.50,
                        key=f"preco_{item['id']}"
                    )

                    if st.button("Salvar preço", key=f"salvar_preco_{item['id']}"):
                        sucesso, mensagem = atualizar_preco_produto(
                            cardapio,
                            item["id"],
                            novo_preco
                        )

                        if sucesso:
                            salvar_cardapio(cardapio)
                            st.success(mensagem)
                            st.rerun()
                        else:
                            st.error(mensagem)

                with col4:
                    if st.button("Alterar status", key=f"alterar_{item['id']}"):
                        sucesso, mensagem = alterar_disponibilidade_produto(
                            cardapio,
                            item["id"]
                        )

                        if sucesso:
                            salvar_cardapio(cardapio)
                            st.success(mensagem)
                            st.rerun()
                        else:
                            st.error(mensagem)

    with aba3:
        nome_produto = st.text_input("Nome do produto")
        preco_produto = st.number_input(
            "Preço do produto",
            min_value=0.00,
            step=0.50
        )

        if st.button("Cadastrar Produto"):
            cardapio = carregar_cardapio()

            sucesso, mensagem, cardapio_atualizado = cadastrar_produto(
                cardapio,
                nome_produto,
                preco_produto
            )

            if sucesso:
                salvar_cardapio(cardapio_atualizado)
                st.success(mensagem)
                st.rerun()
            else:
                st.error(mensagem)