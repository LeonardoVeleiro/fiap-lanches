from models.pagamento_model import Pagamento
from services.banco_service import carregar_json, salvar_json
from models.pagamento_model import Pagamento

ARQUIVO_PEDIDOS = "src/data/pedidos.json"


def carregar_pedidos():
    return carregar_json(ARQUIVO_PEDIDOS, [])


def salvar_pedidos(pedidos):
    salvar_json(ARQUIVO_PEDIDOS, pedidos)


def calcular_total_carrinho(carrinho):
   total = 0
   itens_formatados = []

   for item_id, dados in list(carrinho.items()):
       produto = dados["produto"]
       qtd = dados["qtd"]

       if qtd > 0:
           if not produto["disponivel"]:
               continue

           subtotal = produto["preco"] * qtd
           total += subtotal

           itens_formatados.append({
               "id": produto["id"],
               "nome": produto["nome"],
               "preco": produto["preco"],
               "quantidade": qtd,
               "subtotal": subtotal
           })

   return total, itens_formatados


def criar_pedido(pedidos, usuario_logado, itens_formatados, total, forma_pagamento):
   pagamento = Pagamento(forma_pagamento, total)
   pagamento.processar_pagamento()

   novo_pedido = {
       "id": len(pedidos) + 1,
       "usuario": usuario_logado["nome"],
       "itens": itens_formatados,
       "total": total,
       "pagamento": pagamento.to_dict(),
       "status": "Na fila"
   }

   return novo_pedido


def finalizar_pedido(carrinho, pedidos, usuario_logado, forma_pagamento):
   total, itens_formatados = calcular_total_carrinho(carrinho)

   if not itens_formatados:
       return None, total, "Seu carrinho está vazio ou possui apenas itens indisponíveis."

   novo_pedido = criar_pedido(
       pedidos,
       usuario_logado,
       itens_formatados,
       total,
       forma_pagamento
   )

   pedidos.append(novo_pedido)

   return pedidos, total, None


def filtrar_pedidos_usuario(pedidos, usuario_logado):
   return [
       pedido for pedido in pedidos
       if pedido["usuario"] == usuario_logado["nome"]
   ]
