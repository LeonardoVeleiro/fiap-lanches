import streamlit as st

from services.pedido_service import (
   calcular_total_carrinho,
   finalizar_pedido,
   filtrar_pedidos_usuario
)

#Assinatura:
def exibir_tela_cliente(carregar_cardapio, carregar_pedidos, salvar_pedidos):
   usuario_logado = st.session_state["usuario"]

#Cardápio e pesquisa:
cardapio = carregar_cardapio()

pesquisa = st.text_input(
   "",
   placeholder="Ex: coxinha, pastel, refrigerante..."
)

cardapio_filtrado = [
   item for item in cardapio
   if pesquisa.lower() in item["nome"].lower()
]

#Carrinho:
if "carrinho" not in st.session_state or not isinstance(st.session_state["carrinho"], dict):
   st.session_state["carrinho"] = {}

#Finalizar pedido:
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

#Meus pedidos:
pedidos = carregar_pedidos()
meus_pedidos = filtrar_pedidos_usuario(pedidos, usuario_logado)
