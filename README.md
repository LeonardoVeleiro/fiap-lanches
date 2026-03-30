# 🍔 FIAP Lanches (SmartCantina)

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Vers%C3%A3o%201.0-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> **Otimizando o intervalo acadêmico com tecnologia, autoatendimento e gestão inteligente de filas.**

## 📌 Descrição do Problema
Atualmente, as cantinas universitárias enfrentam grande dificuldade com a alta demanda em curtos intervalos. Isso gera filas extensas, aumento do tempo de espera e estresse para os alunos, que possuem pouco tempo para se alimentar. Além disso, a falta de mão de obra encarece a operação e dificulta o atendimento eficiente, resultando em sobrecarga na equipe.

## 🚀 Solução Proposta e Valor de Negócio
O **FIAP Lanches** é um aplicativo mobile que permite que alunos e colaboradores realizem pedidos e pagamentos antecipadamente. 

Com isso, o sistema atua em duas frentes fundamentais:
1. **Experiência do Usuário:** Elimina-se a necessidade de filas e otimiza-se o tempo do cliente, que apenas retira o pedido quando estiver pronto.
2. **Gestão da Operação:** Melhora a organização da cozinha através de uma fila digital cronológica (KDS - *Kitchen Display System*) e permite o controle de estoque em tempo real.

---

## 🛠 Tecnologias Utilizadas
* **Linguagem:** Python
* **Paradigmas e Estruturas:** Programação Orientada a Objetos (POO), `dataclasses`, `enum`
* **Persistência de Dados:** Arquivos JSON (simulando banco de dados)
* **Ambiente de Execução:** Google Colab / Terminal Local
* **Versionamento:** Git e GitHub

---

## 📁 Estrutura do Projeto

O projeto está arquitetado em dois módulos principais distintos, separando a documentação técnica da aplicação funcional:

### 1. Sistema Funcional - Versão 1.0 (`main.py`)
Este é o núcleo do aplicativo, simulado via terminal interativo. Ele é responsável por orquestrar a interação com os usuários e a persistência de dados.
* **Módulo Cliente:** Interface onde o aluno ou colaborador insere o RM, visualiza o cardápio (filtrado por disponibilidade), adiciona itens ao carrinho e realiza o checkout.
* **Módulo Cantina (Gerente):** Painel administrativo protegido por senha para visualização da fila de preparo (FIFO) e controle em tempo real do estoque (ativar/desativar pratos).
* **Persistência (`banco_cantina.json`):** Arquivo gerado dinamicamente para salvar o histórico de pedidos e o status atualizado do cardápio.

### 2. Especificação de Requisitos (`srs.py`)
Este script é focado na Engenharia de Software do projeto, gerando o documento SRS (*Software Requirements Specification*) de forma programática utilizando POO.
* **Prioridade:** `Enum` para classificação de prioridade dos requisitos (Alta, Média, Baixa).
* **RequisitoFuncional:** Estrutura (`dataclass`) que modela os Requisitos Funcionais do sistema.
* **RequisitoNaoFuncional:** Estrutura (`dataclass`) que modela os Requisitos Não-Funcionais (Desempenho, Segurança, etc.).
* **SRS:** Classe central que cadastra as listas de requisitos e imprime o relatório consolidado e formatado no terminal.

---

## ⚙️ Como Executar

Você pode executar este projeto no **Google Colab** ou em um **ambiente Python local**.

**Para rodar o Aplicativo da Cantina (Versão 1.0):**
1. Copie o código do arquivo `main.py` para a sua IDE.
2. Execute o script no terminal: `python main.py`
3. Siga as instruções do menu interativo para navegar entre os módulos de Cliente e Gerente.

**Para rodar o Relatório de Requisitos (SRS):**
1. Copie o código do arquivo `srs.py` para o Google Colab ou sua IDE.
2. Execute todas as células ou rode o script.
3. Ao final, a chamada `srs.relatorio()` exibirá o relatório completo e formatado dos requisitos na saída do terminal.

---

## 🧩 Funcionalidades Implementadas

O protótipo atende ao núcleo funcional do projeto, englobando:
- [x] Cadastro e autenticação de usuários via RM.
- [x] Visualização de cardápio categorizado.
- [x] Detecção de localização por GPS (simulada).
- [x] Gestão de estoque diário (ativar/desativar pratos).
- [x] Pagamentos via cartão, Pix e vale-alimentação.
- [x] Notificações de status do pedido.
- [x] CRUD de cardápio para gerentes.
- [x] Controle de acesso (RBAC - acessos restritos por senha).
- [x] Relatórios de vendas.
- [x] Configuração de horário de funcionamento.
- [x] Organização de pedidos por ordem de chegada na cozinha (Fila FIFO).

---

## 📸 Demonstração

Abaixo estão os registros do sistema operando via terminal, cobrindo os principais fluxos do cliente e da gestão:

* 🎓 **Visão do Aluno (Pedido e Pagamento VA):** Entrou como aluno, pediu o prato feito e pagou com vale-alimentação. 
  👉 [Ver imagem](https://prnt.sc/V0j9sA_ZLlB7)
* 🎓 **Visão do Aluno (Múltiplos Itens e PIX):** Entrada como aluno, pediu dois itens e pagou com PIX. 
  👉 [Ver imagem](https://prnt.sc/O32g9APKsxji)
* 🍔 **Visão da Gerência (KDS e Baixa de Fila):** Entrou como gerente, visualizou a fila de pedidos e anunciou o pedido #2 como pronto. 
  👉 [Ver imagem](https://prnt.sc/3yzqvxuGvEJu)
* 🍔 **Visão da Gerência (Gestão de Estoque):** Entrou como gerente e pausou um dos itens do cardápio (o prato feito) que esgotou no dia. 
  👉 [Ver imagem](https://prnt.sc/iisDFRr1H0Hl)

---

## 👨‍💻 Integrantes do Grupo

* **Agatha Cassari**
* **Gustavo Cheng**
* **Leonardo Veleiro**
* **Sara Barbosa**

## 🔗 Links Oficiais
* 🎨 **Board no Miro (Diagramas e Planejamento):** [Acessar Miro](https://miro.com/app/board/uXjVGwHZNKQ=/)
