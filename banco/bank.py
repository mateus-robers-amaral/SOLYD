''' Crie um software de gerenciamento bancário.
Este poderá ser capaz de criar clientes e contas
cada cliente possui nome, cpf e idade
e cada conta possui um client, um saldo, limite, sacar, depositar e consultar saldo'''
import random
import csv

class Cliente():
    def __init__(self, nome, cpf, idade, conta, saldo):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.conta = conta
        self.saldo = saldo
    
class Conta(Cliente):
    def criar_conta(self, conta):
        self.conta = random.randint(10000000000,99999999999)
        print(conta)

    # def acessar_conta(self, conta):
    #     for i in contas:

#def salvar_conta():
