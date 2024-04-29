from bank import Conta
import random

print("[1] Criar nova conta\n[2] Acessar conta já existente")
resp = int(input("-> "))

if resp == 1:
        while True:
                nome = input('Informe seu nome:\n-> ')
                if nome.isdigit():
                        print('Digite apenas letras.')
                        continue
                else:
                        break
        while True:
                cpf = input('Informe seu CPF sem "-" e ".":\n-> ')
                if len(cpf) != 11:
                        print('CPF inválido. O CPF deve conter 11 números.')
                        continue
                elif cpf.isalpha():
                        print('O CPF deve conter apenas algorismos numéricos.')
                        continue
                else:
                        break
        while True:
                try:
                        idade = int(input('Informe sua idade:\n-> '))
                        if idade < 18:
                                print('A idade mínima para criar uma conta é 18 anos.')
                                exit()
                        else:
                                break

                except ValueError:
                        print('Digite apenas números')
                        continue
numero_conta = str(random.randint(0,9999999999)).zfill(4)

with open("contas.csv", "r") as file:
        for linha in file:
                dados_conta = linha.strip().split(",")