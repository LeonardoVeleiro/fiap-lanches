class Usuario:
  def __init__(self, nome, email, rm, senha, perfil="cliente"):
    self.nome = nome
    self.email = email
    self.rm = rm
    self.senha = senha
    self.perfil = perfil
  def to_dict(self):
    return {
      "nome": self.nome,
      "email": self.email,
      "rm": self.rm,
      "senha": self.senha,
      "perfil": self.perfil
    }
@staticmethod
def from_dict(dado):
  return Usuario(
    dado["nome"],
    dado["email"],
    dado["rm"],
    dado["senha"],
    dado["perfil"]
)
