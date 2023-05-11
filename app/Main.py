class Main:
    pass


from Cliente import Cliente
from Conta import Conta

c1= Cliente("Joao","1197652300")
conta=Conta(c1.nome,15400,100)
#imprimeindo os valores
#print(c1)
print(c1.nome)
print("Telefone do ",c1.nome,":",c1.telefone)
print("Nome do titular: ", conta.titular)
print("Numero da conta:",conta.numero)
print("Saldo dísponível: R$ ",conta.saldo)
