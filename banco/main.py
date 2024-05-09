from bank import Cliente
import csv

print("[1] Criar nova conta\n[2] Acessar conta já existente")
resp = int(input("-> "))

if resp == 1:
        validacao = Cliente.validar()
        cliente1 = Cliente(validacao[0], validacao[1], validacao[2], validacao[3])
        cliente1.criar_conta()

elif resp == 2:
        Cliente.acessar_conta()
        