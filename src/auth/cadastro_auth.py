import hashlib
from services.banco_service import carregar_json, salvar_json

ARQUIVO_USUARIOS = "src/data/usuarios.json"


def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def validar_dados_cadastro(nome, email, rm, senha, confirmar_senha):
    if not nome or not email or not rm or not senha or not confirmar_senha:
        return False, "Preencha todos os campos."

    if "@" not in email or "." not in email:
        return False, "Digite um e-mail válido."

    if not rm.isdigit():
        return False, "O RM deve conter apenas números."

    if len(senha) < 4:
        return False, "A senha deve ter pelo menos 4 caracteres."

    if senha != confirmar_senha:
        return False, "As senhas não conferem."

    return True, ""


def cadastrar_usuario(nome, email, rm, senha, confirmar_senha):
    valido, mensagem = validar_dados_cadastro(
        nome,
        email,
        rm,
        senha,
        confirmar_senha
    )

    if not valido:
        return False, mensagem

    usuarios = carregar_json(ARQUIVO_USUARIOS, [])

    for usuario in usuarios:
        if usuario["email"] == email or usuario["rm"] == rm:
            return False, "E-mail ou RM já cadastrado."

    novo_usuario = {
        "nome": nome,
        "email": email,
        "rm": rm,
        "senha": gerar_hash(senha),
        "perfil": "cliente"
    }

    usuarios.append(novo_usuario)
    salvar_json(ARQUIVO_USUARIOS, usuarios)

    return True, "Usuário cadastrado com sucesso!"
