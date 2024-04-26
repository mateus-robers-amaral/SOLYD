from exercicio1 import Cliente, criar_conta, acessar_conta
import random

print("Olá, selecione a opção que desejas:\n[1] Criar nova conta\n[2] Acessar conta já existente")
resp = int(input("-> "))

if resp == 1:
        criar_conta()
elif resp == 2:
        acessar_conta()
