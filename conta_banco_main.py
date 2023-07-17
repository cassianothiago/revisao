from conta_banco import*
from os import system

print('-----')
print('Bem vindo ao cadastro de conta')
print('-----')
agencia=input('Digite a agência = ')
conta=input('Digite a conta = ')
nome=input('Digite o nome = ')
cpf=int(input('Digite o CPF = '))
fone=int(input('Digite o numero do telefone = '))
senha=int(input('Digite sua senha = '))
saldo=0
cadastro=Conta_Banco(agencia,conta,nome,cpf,fone,senha,saldo)
system('pause')
print('cadastro efetuado com sucesso')
system('pause')
system('cls')
print('-----')
print('Bem vindo ao Banco')
while True:
    menu=int(input('Digite\n1 para deposito\n2 Para extrato\n3 Para saque\n0 (zero) encerrar\n:. '))
    if menu==1:
        deposito=float(input('valor para deposito = '))
        cadastro.deposito(deposito)
        system('pause')
        system('cls')
    if menu==2:
        dig_senha=int(input('digite sua senha = '))
        cadastro.extrato(dig_senha)
        system('pause')
        system('cls')
    if menu==3:
        dig_senha=int(input('digite sua senha = '))
        valor_saque=int(input('digite o valor do saque = '))
        cadastro.saque(dig_senha,valor_saque)
        system('pause')
        system('cls')
    elif menu==0:
        print('obrigado por utilizar o banco')
        break
    system('pause')
    system('cls')
    
    

