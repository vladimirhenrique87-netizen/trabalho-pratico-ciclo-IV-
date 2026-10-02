# Sistema de Atendimento e Pedidos em Lanchonete

## Identificação
* **Nome do Estudante:** [Vladimir Henrique De Resende]
* **Disciplina:** Algoritmos e Programação

## Descrição do Projeto
Este projeto consiste em um sistema de atendimento desenvolvido em Python para automatizar os pedidos de uma lanchonete. O software interage com o usuário para registrar produtos, calcular valores, aplicar regras progressivas de desconto, processar o pagamento e emitir um resumo completo da compra.

## Principais Funcionalidades
1. **Identificação do Cliente:** Captura o nome do cliente no início da execução.
2. **Cardápio Interativo:** Exibe opções de produtos com códigos e preços fixos.
3. **Acumulação Dinâmica:** Calcula subtotais e soma o valor total sem o uso de listas ou dicionários.
4. **Validação de Dados:** Trata entradas incorretas (códigos inválidos, quantidades negativas e opções de pagamento erradas).
5. **Regras de Desconto:** Aplicação automática de descontos com base no valor total (0% para abaixo de R$ 50,00; 5% de R$ 50,00 a R$ 99,99; 10% para R$ 100,00 ou mais).
6. **Organização Modular:** Código estruturado por meio de funções reutilizáveis.

## Instruções de Execução
1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python main.py
