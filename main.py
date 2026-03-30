# ============================================================
# 🚀 SRS
# Projeto: FIAP Lanches
# ============================================================
from dataclasses import dataclass, field
from typing import List
from enum import Enum

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str

@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str  # Desempenho, Segurança, Usabilidade...
    descricao: str
    prioridade: Prioridade # Adicionado o atributo Prioridade aqui
    criterio_aceitacao: str

@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*70}")
        print(f"📋 SRS — {self.projeto} v{self.versao}")
        print(f"{'='*70}")
        print(f"📝 {self.descricao}\n")

        print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"       Ator: {rf.ator}")
            print(f"       📌 {rf.descricao}")
            print(f"       Pré-condição: {rf.pre_condicao}")
            print(f"       Pós-condição: {rf.pos_condicao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"  [{rnf.id}] {rnf.categoria} — Prioridade: {rnf.prioridade.value}") # Atualizado o print aqui
            print(f"       📌 {rnf.descricao}")
            print(f"       ✔️  Critério: {rnf.criterio_aceitacao}\n")

# ---- Criando o SRS do App FIAP Lanches ----
srs = SRS(
    projeto="FIAP Lanches (App de Pedidos na Cantina)",
    versao="1.0",
    descricao="Sistema mobile de autoatendimento para pedidos antecipados na cantina, visando a redução de filas nos intervalos."
)

print("Iniciando a carga de requisitos...\n")
srs.adicionar_rf(RequisitoFuncional(
    id="RF-01", nome="Autenticação com RM",
    descricao="Permitir a autenticação de usuários utilizando o RM da instituição.",
    prioridade=Prioridade.ALTA, ator="Cliente / Gerente",
    pre_condicao="Usuário possuir vínculo ativo com a FIAP",
    pos_condicao="Acesso liberado às funcionalidades do app"
))
srs.adicionar_rf(RequisitoFuncional(
    id="RF-02", nome="Exibição de Cardápio",
    descricao="Exibir o cardápio completo de forma categorizada com fotos e preços.",
    prioridade=Prioridade.ALTA, ator="Cliente",
    pre_condicao="Estar logado no sistema",
    pos_condicao="Visualização dos itens disponíveis para compra"
))
srs.adicionar_rf(RequisitoFuncional(
    id="RF-03", nome="Detecção de Unidade (GPS)",
    descricao="Detectar a localização do usuário para identificar a unidade da FIAP.",
    prioridade=Prioridade.MEDIA, ator="Cliente",
    pre_condicao="Permissão de GPS concedida no app",
    pos_condicao="Cardápio filtrado para a unidade atual"
))
srs.adicionar_rf(RequisitoFuncional(
    id="RF-04", nome="Gestão de Estoque Diário",
    descricao="Permitir que a cantina desative pratos que estão em falta no dia.",
    prioridade=Prioridade.ALTA, ator="Gerente",
    pre_condicao="Estar logado como Gerente",
    pos_condicao="Item removido instantaneamente da visão do cliente"
))
srs.adicionar_rf(RequisitoFuncional(
    id="RF-05", nome="Múltiplos Meios de Pagamento",
    descricao="Processar pagamentos via Cartão de Crédito/Débito, PIX e Vale-Alimentação.",
    prioridade=Prioridade.ALTA, ator="Cliente",
    pre_condicao="Ter itens no carrinho e prosseguir para checkout",
    pos_condicao="Pagamento aprovado e pedido gerado"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-06", nome="Notificações de Status",
    descricao="Enviar notificações (Push) do status do pagamento e preparo do pedido.",
    prioridade=Prioridade.MEDIA, ator="Sistema",
    pre_condicao="Pedido realizado e com mudança de status na cozinha",
    pos_condicao="Cliente alertado em seu dispositivo"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-07", nome="Gestão de Cardápio (CRUD)",
    descricao="Módulo para gerentes adicionarem, alterarem ou removerem pratos permanentemente.",
    prioridade=Prioridade.ALTA, ator="Gerente",
    pre_condicao="Acesso ao painel administrativo",
    pos_condicao="Banco de dados do cardápio atualizado"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-08", nome="Controle de Acesso (RBAC)",
    descricao="Implementar níveis de acesso para garantir que apenas gerentes façam modificações sensíveis.",
    prioridade=Prioridade.ALTA, ator="Sistema",
    pre_condicao="Tentativa de acesso a rotas restritas",
    pos_condicao="Validação de permissão concedida ou negada"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-09", nome="Relatórios Gerenciais",
    descricao="Armazenar dados e gerar relatórios de desempenho e vendas diárias.",
    prioridade=Prioridade.BAIXA, ator="Gerente",
    pre_condicao="Existência de pedidos finalizados no banco",
    pos_condicao="Exibição de gráficos e métricas de venda"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-10", nome="Configuração de Horário",
    descricao="Configurar o horário de funcionamento (abertura e fechamento) da cantina.",
    prioridade=Prioridade.MEDIA, ator="Gerente",
    pre_condicao="Acesso às configurações da loja",
    pos_condicao="App bloqueia novos pedidos fora do horário estipulado"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-11", nome="Fila de Pedidos (FIFO - KDS)",
    descricao="Exibir os pedidos para a cozinha organizados estritamente por ordem de chegada.",
    prioridade=Prioridade.ALTA, ator="Gerente / Cozinha",
    pre_condicao="Existência de pedidos pagos e pendentes",
    pos_condicao="Cozinha visualiza a ordem correta de preparo"
))

# --- Adicionando os Requisitos Não-Funcionais (RNF) ---
srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-01", categoria="Usabilidade",
    descricao="O fluxo para repetir um pedido anterior deve exigir no máximo 4 cliques.",
    prioridade=Prioridade.MEDIA, # Prioridade Média
    criterio_aceitacao="Teste de usabilidade com usuário concluindo a tarefa em < 15 segundos."
))
