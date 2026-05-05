import json
import os


def carregar_json(caminho, padrao):
    if not os.path.exists(caminho):
        return padrao

    with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read().strip()
        if not conteudo:
            return padrao
        return json.loads(conteudo)


def salvar_json(caminho, dados):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)