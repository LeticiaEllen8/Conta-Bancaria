class ContaBancaria:
   def __init__(self, cliente, tipoconta, numeroconta, saldo, limite, saque):
      self.cliente = cliente
      self.tipoconta = tipoconta
      self.numeroconta = numeroconta
      self.saldo = saldo
      self.statusconta = False
      self.limite = limite
      self.saque = saque


   def depositar(self, deposito):
      if self.statusconta == True:
          self.deposito = deposito
          print("Sua conta está inativa. Não é possível realizar depósitos.")
      else:
          self.saldo += deposito
          print(f'Opção depósito disponível.\nDeposito de R${deposito} realizado com sucesso.\nNovo saldo de R${self.saldo}')


   def sacar(self, saque):
      if self.statusconta == True:
          self.saque = saque
          print("Sua conta está inativa. Não é possível realizar saques.")
      else:
          self.saldo -= saque
          print(f'Opção saque disponível.\nSaque de R${saque} realizado com sucesso.\nNovo saldo de R${self.saldo}')


   def verificarsaldo(self):
      print(f'Seu saldo atual é de: {self.saldo}.')


   def ativarconta(self):
      if self.statusconta == False:
          self.ativar = True
   ativação = int(input('Sua conta está inativa. Deseja a reativação?\nDigite 1 para SIM ou 2 para NÃO: '))
   if ativação == 1:
       print('Conta reativada com sucesso.')
   else:
       print('Conta permanece desativada.')


   def desativarconta(self):
          if self.saldo == 0:
              desativação = int(input('Saldo: R$ 0,00 \nVocê pode desativar sua conta.\n Digite 1 para SIM ou 2 para NÃO'))
              if desativação == 1:
                  print('Conta desativada com sucesso.')
          else:
              print('Conta permanece ativada.')




conta = ContaBancaria("Fiorella", "Corrente", 410, 500, 2000, 100)
conta.depositar(400)
conta.verificarsaldo()
conta.sacar(100)
conta.ativarconta()
