# =====================================================================
# TRABALHO PRÁTICO — ALGORITMOS E PROGRAMAÇÃO
# Sistema de Atendimento e Pedidos em Python
# =====================================================================


def exibir_cardapio():
    """Exibe o cardápio com os 5 produtos disponíveis."""
    print("\n================ CARDÁPIO DA LANCHONETE ================")
    print("1. Hambúrguer Simples - R$ 15.00")
    print("2. X-Bacon           - R$ 22.50")
    print("3. Batata Frita      - R$ 12.00")
    print("4. Refrigerante      - R$ 6.50")
    print("5. Milkshake         - R$ 14.00")
    print("========================================================")


def obter_nome_produto(codigo):
    """Retorna o nome do produto com base no código utilizando match-case."""
    match codigo:
        case 1:
            return "Hambúrguer Simples"
        case 2:
            return "X-Bacon"
        case 3:
            return "Batata Frita"
        case 4:
            return "Refrigerante"
        case 5:
            return "Milkshake"
        case _:
            return ""


def obter_preco_produto(codigo):
    """Retorna o preço do produto com base no código utilizando match-case."""
    match codigo:
        case 1:
            return 15.00
        case 2:
            return 22.50
        case 3:
            return 12.00
        case 4:
            return 6.50
        case 5:
            return 14.00
        case _:
            return 0.0


def calcular_percentual_desconto(total):
    """Calcula o percentual de desconto com base no valor total da compra."""
    if total >= 100.00:
        return 10
    elif total >= 50.00:
        return 5
    else:
        return 0


def obter_forma_pagamento():
    """Solicita e valida a forma de pagamento escolhida pelo cliente."""
    while True:
        print("\nForma de Pagamento:")
        print("1. Dinheiro")
        print("2. PIX")
        print("3. Cartão")

        opcao = int(input("Escolha a forma de pagamento (1-3): "))

        match opcao:
            case 1:
                return "Dinheiro"
            case 2:
                return "PIX"
            case 3:
                return "Cartão"
            case _:
                print(
                    "\n[ERRO] Opção de pagamento inválida! Tente novamente."
                )


def main():
    print("=== BEM-VINDO AO SISTEMA DE ATENDIMENTO ===")
    nome_cliente = input("Digite o nome do cliente: ")

    total_compra = 0.0

    # Estrutura de repetição para continuar o atendimento
    while True:
        exibir_cardapio()
        codigo = int(input("Digite o código do produto desejado: "))

        # Validação do código do produto
        nome_produto = obter_nome_produto(codigo)
        preco_produto = obter_preco_produto(codigo)

        if preco_produto == 0.0:
            print(
                "\n[ERRO] Código de produto inválido! Por favor, escolha um código do cardápio."
            )
            continue

        # Entrada e validação da quantidade
        quantidade = int(input(f"Digite a quantidade de '{nome_produto}': "))
        if quantidade <= 0:
            print(
                "\n[ERRO] Quantidade inválida! A quantidade deve ser maior que zero."
            )
            continue

        # Cálculo do subtotal e acumulação no total da compra
        subtotal = preco_produto * quantidade
        total_compra += subtotal

        print(
            f"\n[SUCESSO] Adicionado: {quantidade}x {nome_produto} | Subtotal: R$ {subtotal:.2f}"
        )

        # Pergunta se deseja continuar comprando
        continuar = input(
            "\nDeseja adicionar mais algum produto? (S/N): "
        ).strip().upper()
        if continuar != "S":
            break

    # Cálculo de descontos
    percentual_desconto = calcular_percentual_desconto(total_compra)
    valor_desconto = total_compra * (percentual_desconto / 100)
    valor_final = total_compra - valor_desconto

    # Forma de pagamento
    forma_pagamento = obter_forma_pagamento()

    # Resumo final do atendimento
    print("\n================ RESUMO DO ATENDIMENTO ================")
    print(f"Cliente: {nome_cliente}")
    print(f"Valor original da compra: R$ {total_compra:.2f}")
    print(f"Desconto aplicado: {percentual_desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print("=======================================================")
    print("Obrigado pela preferência! Volte sempre.")


# Execução do programa principal
if __name__ == "__main__":
    main()
