import hashlib
from services.banco_service import carregar_json

ARQUIVO_USUARIOS = "src/data/usuarios.json"


def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def validar_dados_login(rm, senha):
    if not rm or not senha:
        return False, "Preencha todos os campos."

    if not rm.isdigit():
        return False, "O RM deve conter apenas números."

    return True, ""


def login_usuario(rm, senha):
    valido, mensagem = validar_dados_login(rm, senha)

    if not valido:
        return False, mensagem

    usuarios = carregar_json(ARQUIVO_USUARIOS, [])
    senha_hash = gerar_hash(senha)

    for usuario in usuarios:
        if usuario["rm"] == rm and usuario["senha"] == senha_hash:
            return True, usuario

    return False, "RM ou senha inválidos."
