def listar_pedidos_na_fila(pedidos):
    return [
        pedido for pedido in pedidos
        if pedido["status"] == "Na fila"
    ]


def marcar_pedido_como_pronto(pedidos, id_pedido):
    for pedido in pedidos:
        if pedido.get("id") == id_pedido:
            pedido["status"] = "Pronto"
            return True, "Pedido pronto!"

    return False, "Pedido não encontrado."


def atualizar_preco_produto(cardapio, id_produto, novo_preco):
    if novo_preco <= 0:
        return False, "O preço do produto deve ser maior que zero."

    for item in cardapio:
        if item["id"] == id_produto:
            item["preco"] = novo_preco
            return True, "Preço atualizado!"

    return False, "Produto não encontrado."


def alterar_disponibilidade_produto(cardapio, id_produto):
    for item in cardapio:
        if item["id"] == id_produto:
            item["disponivel"] = not item["disponivel"]
            return True, "Status atualizado!"

    return False, "Produto não encontrado."


def cadastrar_produto(cardapio, nome_produto, preco_produto):
    nome = nome_produto.strip()

    if not nome:
        return False, "O nome do produto não pode ser vazio.", None

    if preco_produto <= 0:
        return False, "O preço do produto não pode ser zero.", None

    ja_existe = any(
        item["nome"].lower().strip() == nome.lower()
        for item in cardapio
    )

    if ja_existe:
        return False, "Produto já existe no cardápio.", None

    novo_id = max([item["id"] for item in cardapio], default=0) + 1

    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "preco": preco_produto,
        "disponivel": True
    }

    cardapio.append(novo_produto)

    return True, f"Produto '{nome}' cadastrado com sucesso!", cardapio