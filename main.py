# ============================================================
# SRS em Python — Projeto: FIAP Lanches - Gustavo Cheng
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
    categoria: str
    descricao: str
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
        print(f"RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*60}")
        print(f"SRS — {self.projeto} v{self.versao}")
        print(f"{'='*60}")
        print(f"{self.descricao}\n")

        print(f"REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"[{rf.id}] {rf.nome} — {rf.prioridade.value}")
            print(f"Ator: {rf.ator}")
            print(f"Descrição: {rf.descricao}")
            print(f"Pré-condição: {rf.pre_condicao}")
            print(f"Pós-condição: {rf.pos_condicao}\n")

        print(f"REQUISITOS NÃO FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"[{rnf.id}] {rnf.categoria}")
            print(f"Descrição: {rnf.descricao}")
            print(f"Critério: {rnf.criterio_aceitacao}\n")


# ---- Criando o SRS ----
srs = SRS(
    projeto="FIAP Lanches",
    versao="1.0",
    descricao="App de pedidos antecipados para cantina, reduzindo filas e otimizando o atendimento."
)

# ---- Requisitos Funcionais ----
srs.adicionar_rf(RequisitoFuncional(
    "RF-01", "Autenticação",
    "Permitir login utilizando RM.",
    Prioridade.ALTA, "Cliente",
    "Usuário cadastrado",
    "Usuário autenticado"
))

srs.adicionar_rf(RequisitoFuncional(
    "RF-02", "Cardápio",
    "Exibir cardápio com categorias e preços.",
    Prioridade.ALTA, "Cliente",
    "Usuário logado",
    "Itens exibidos"
))

srs.adicionar_rf(RequisitoFuncional(
    "RF-03", "Pagamento",
    "Permitir pagamento via Pix, cartão e VA.",
    Prioridade.ALTA, "Cliente",
    "Pedido criado",
    "Pagamento aprovado"
))

# ---- Requisitos Não Funcionais ----
srs.adicionar_rnf(RequisitoNaoFuncional(
    "RNF-01", "Usabilidade",
    "Repetir pedido em até 4 cliques.",
    "Usuário conclui em menos de 15s"
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    "RNF-02", "Desempenho",
    "Atualização da cozinha em menos de 2s.",
    "Latência < 2000ms"
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    "RNF-03", "Segurança",
    "Criptografia dos dados de pagamento.",
    "Uso de TLS"
))

# ---- Gerar relatório ----
srs.relatorio()
