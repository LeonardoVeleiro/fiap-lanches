class Produto:
   def __init__(self, id, nome, preco, disponivel=True):
       self.id = id
       self.nome = nome
       self.preco = preco
       self.disponivel = disponivel

   def to_dict(self):
       return {
           "id": self.id,
           "nome": self.nome,
           "preco": self.preco,
           "disponivel": self.disponivel
       }

   @staticmethod
   def from_dict(dado):
       return Produto(
           dado["id"],
           dado["nome"],
           dado["preco"],
           dado["disponivel"]
       )
