from exercicio1 import Cliente, criar_conta
import random

print("Olá, selecione a opção que desejas:\n[1] Criar nova conta\n[2] Acessar conta já existente")
resp = int(input("-> "))

if resp == 1:
        cadastro = Cliente(input("Qual o seu nome?\n-> "), input("Digite seu CPF:\n-> "), input("Qual a sua idade?\n-> "), criar_conta())
elif resp == 2:
        acessar_conta()
