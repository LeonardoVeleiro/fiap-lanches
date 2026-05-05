from datetime import datetime


class Pedido:
   def __init__(self, id, usuario, itens, total, status="Na fila", hora=None):
       self.id = id
       self.usuario = usuario
       self.itens = itens
       self.total = total
       self.status = status
       self.hora = hora or datetime.now().strftime("%H:%M:%S")

   def marcar_como_pronto(self):
       self.status = "Pronto"

   def to_dict(self):
       return {
           "id": self.id,
           "usuario": self.usuario,
           "itens": [item.to_dict() for item in self.itens],
           "total": self.total,
           "status": self.status,
           "hora": self.hora
       }

   @staticmethod
   def from_dict(dado):
       from models.produto_model import Produto

       itens = [Produto.from_dict(i) for i in dado["itens"]]

       return Pedido(
           dado["id"],
           dado["usuario"],
           itens,
           dado["total"],
           dado["status"],
           dado["hora"]
       )
