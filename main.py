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
