class Aluno:
   def __init__(self,Nome,Nascimento,Sexo,Serie,CEP,CPF,Mae,Pai,Responsavel,TelResp,Necessidades):
      self.Nome = Nome
      self.Nascimento = Nascimento
      self.Sexo = Sexo
      self.Serie = Serie
      self.CEP = CEP
      self.CPF = CPF
      self.Mae = Mae
      self.Pai = Pai
      self.Responsavel = Responsavel
      self.TelResp = TelResp
      self.Necessidades = Necessidades

   def ver(self):
      print(f"Informações do Aluno: \n Nome: {self.Nome} \n Data de Nascimento: {self.Nascimento} \n")
      print(f"Sexo: {self.Sexo} \n Série: {self.Serie} \n CEP: {self.CEP} CPF: {self.CPF} \n")
      print(f"Mãe: {self.Mae} \n Pai: {self.Pai} \n Responsável: {self.Responsavel} \n")
      print(f"Telefone do Responsável: {self.TelResp} \n Necessidades: {self.Necessidades}\n")

