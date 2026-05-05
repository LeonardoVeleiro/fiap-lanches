class Pagamento:
   def __init__(self, forma_pagamento, valor, status="Pendente"):
       self.forma_pagamento = forma_pagamento
       self.valor = valor
       self.status = status

   def processar_pagamento(self):
       self.status = "Aprovado"
       return True

   def to_dict(self):
       return {
           "forma_pagamento": self.forma_pagamento,
           "valor": self.valor,
           "status": self.status
       }

   @staticmethod
   def from_dict(dado):
       return Pagamento(
           dado["forma_pagamento"],
           dado["valor"],
           dado["status"]
       )
