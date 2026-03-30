# --- MÓDULO DO CLIENTE (ALUNO/COLABORADOR) ---
def modulo_cliente(dados):
    print("\n=== ÁREA DO CLIENTE ===")
    rm = input("Digite seu RM para entrar (RF01): ").strip()
    if not rm.isdigit():
        print("❌ RM Inválido. Apenas números.")
        return

    # Simulando Geolocalização (RF03)
    print("\n📍 Unidade detectada: FIAP Paulista (GPS)")

    # Listar apenas itens disponíveis (RF04)
    print("\n--- Cardápio do Dia ---")
    cardapio = dados["cardapio"]
    itens_ativos = {k: v for k, v in cardapio.items() if v["disponivel"]}

    for k, v in itens_ativos.items():
        print(f"[{k}] {v['nome']} - R$ {v['preco']:.2f}")

    carrinho = []
    total = 0.0

    while True:
        escolha = input("\nEscolha um item (ou '0' para pagar): ")
        if escolha == '0': break
        if escolha in itens_ativos:
            carrinho.append(itens_ativos[escolha]['nome'])
            total += itens_ativos[escolha]['preco']
            print(f"✅ Adicionado! Subtotal: R$ {total:.2f}")
        else:
            print("❌ Opção inválida ou indisponível hoje.")

    if carrinho:
        print(f"\nTotal: R$ {total:.2f}")
        print("Opções: [1] PIX [2] Cartão [3] Vale-Alimentação (RF05)")
        pagamento = input("Forma de pagamento: ")

        # Gera o pedido e coloca na fila (RF11)
        novo_pedido = {
            "id": len(dados["pedidos"]) + 1,
            "rm": rm,
            "itens": carrinho,
            "hora": datetime.now().strftime("%H:%M:%S"),
            "status": "Na Fila"
        }
        dados["pedidos"].append(novo_pedido)
        salvar_banco(dados)
        print(f"\n🔔 Pagamento Aprovado! Pedido #{novo_pedido['id']} enviado para a cozinha (RF06).")
