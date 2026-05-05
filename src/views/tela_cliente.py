import streamlit as st

from services.cardapio_service import carregar_cardapio
from services.pedido_service import (
    carregar_pedidos,
    salvar_pedidos,
    calcular_total_carrinho,
    finalizar_pedido,
    filtrar_pedidos_usuario
)


def exibir_tela_cliente():
    usuario_logado = st.session_state["usuario"]

    st.header("Área do Cliente")

    aba1, aba2 = st.tabs(["Cardápio", "Meus Pedidos"])

    with aba1:
        st.subheader("Cardápio")

        cardapio = carregar_cardapio()

        if not cardapio:
            st.warning("Nenhum item cadastrado no cardápio.")
            return

        pesquisa = st.text_input(
            "",
            placeholder="Ex: coxinha, pastel, refrigerante..."
        )

        cardapio_filtrado = [
            item for item in cardapio
            if pesquisa.lower() in item["nome"].lower()
        ]

        if "carrinho" not in st.session_state or not isinstance(st.session_state["carrinho"], dict):
            st.session_state["carrinho"] = {}

        if not cardapio_filtrado:
            st.warning("Nenhum item encontrado.")

        for item in cardapio_filtrado:
            item_id = item["id"]

            if item_id not in st.session_state["carrinho"]:
                st.session_state["carrinho"][item_id] = {
                    "produto": item,
                    "qtd": 0
                }

            # Atualiza o produto no carrinho caso o gerente mude preço/disponibilidade
            st.session_state["carrinho"][item_id]["produto"] = item

            col1, col2 = st.columns([4, 2])

            with col1:
                status = ""

                if not item["disponivel"]:
                    status = "<p style='color:red; font-weight:bold;'>Indisponível</p>"

                st.markdown(f"""
                <div class="card">
                    <div class="card-title">{item['nome']}</div>
                    <div class="price">R$ {item['preco']:.2f}</div>
                    {status}
                </div>
                """, unsafe_allow_html=True)

            with col2:
                qtd = st.session_state["carrinho"][item_id]["qtd"]

                col_menos, col_qtd, col_mais = st.columns([1, 1, 1])

                with col_menos:
                    if st.button("-", key=f"menos_{item_id}"):
                        if qtd > 0:
                            st.session_state["carrinho"][item_id]["qtd"] -= 1
                            st.rerun()

                with col_qtd:
                    st.markdown(
                        f"<h4 style='text-align:center;'>{qtd}</h4>",
                        unsafe_allow_html=True
                    )

                with col_mais:
                    if item["disponivel"]:
                        if st.button("+", key=f"mais_{item_id}"):
                            st.session_state["carrinho"][item_id]["qtd"] += 1
                            st.rerun()
                    else:
                        st.button("+", key=f"mais_{item_id}", disabled=True)

        st.divider()

        st.subheader("🛒 Carrinho")

        total, itens_formatados = calcular_total_carrinho(
            st.session_state["carrinho"]
        )

        for item in itens_formatados:
            st.markdown(f"""
            <div class="card">
                <strong>{item['nome']}</strong><br>
                Quantidade: {item['quantidade']}<br>
                Subtotal: R$ {item['subtotal']:.2f}
            </div>
            """, unsafe_allow_html=True)

        if not itens_formatados:
            st.info("Seu carrinho está vazio.")

        st.write(f"**Total: R$ {total:.2f}**")

        forma_pagamento = st.selectbox(
            "Forma de pagamento",
            ["PIX", "Cartão de Débito", "Cartão de Crédito", "Vale-Alimentação"]
        )

        if st.button("Finalizar Pedido"):
            pedidos = carregar_pedidos()

            pedidos_atualizados, total, erro = finalizar_pedido(
                st.session_state["carrinho"],
                pedidos,
                usuario_logado,
                forma_pagamento
            )

            if erro:
                st.error(erro)
            else:
                salvar_pedidos(pedidos_atualizados)

                st.success("Pagamento aprovado! Pedido enviado para a fila.")
                st.balloons()
                st.session_state["carrinho"] = {}
                st.rerun()

    with aba2:
        st.subheader("Meus Pedidos")

        pedidos = carregar_pedidos()
        meus_pedidos = filtrar_pedidos_usuario(pedidos, usuario_logado)

        if not meus_pedidos:
            st.info("Você ainda não realizou nenhum pedido.")
        else:
            for pedido in reversed(meus_pedidos):
                numero_pedido = pedido.get("id", "sem número")

                if pedido["status"] == "Pronto":
                    st.success(f"Pedido #{numero_pedido} está pronto para retirada!")
                else:
                    st.warning(f"Pedido #{numero_pedido} está {pedido['status']}.")

                st.write(f"Total: R$ {pedido['total']:.2f}")

                with st.expander("Ver itens do pedido"):
                    for item in pedido["itens"]:
                        quantidade = item.get("quantidade", 1)
                        subtotal = item.get("subtotal", item["preco"] * quantidade)

                        st.write(
                            f"- {item['nome']} | Qtd: {quantidade} | "
                            f"R$ {item['preco']:.2f} | Subtotal: R$ {subtotal:.2f}"
                        )