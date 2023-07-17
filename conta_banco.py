class Conta_Banco():
    def __init__(self,agencia,conta,nome,cpf,fone,senha,saldo):
        self.agencia=agencia
        self.conta=conta
        self.nome=nome
        self.__cpf=cpf
        self.fone=fone
        self.__senha=senha
        self.__saldo=saldo
        
    def deposito(self,dep):
        self.__saldo=self.__saldo+dep
        print('Deposito efetuado com sucesso')
        
    def extrato(self,senha):
        if senha!=self.__senha:
            print('Senha invalida')
        elif senha==self.__senha:
            print('Saldo = ',self.__saldo)
        else:
            print('Erro senha')
    
    def saque(self,senha,valor):
        if senha!=self.__senha:
            print('Senha invalida')
        elif senha==self.__senha:
            print('Valor do saque = ',valor)
            self.__saldo=self.__saldo-valor
            if valor>self.__saldo:
                print('saldo insuficiente')
            else:
                print('Saldo = ',self.__saldo)
        else:
            print('Erro senha')
        
        