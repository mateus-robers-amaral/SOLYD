''' Crie um software de gerenciamento bancário.
Este poderá ser capaz de criar clientes e contas
cada cliente possui nome, cpf e idade
e cada conta possui um client, um saldo, limite, sacar, depositar e consultar saldo'''
import csv

class Cliente():
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    
    def validar():
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
                
        return [nome, cpf, idade]

    def criar_conta(self):
        
        num_conta = 1000000
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='r') as arquivo:
               leitor_csv = csv.reader(arquivo)
               for linha in leitor_csv:
                      num_conta += 1
                                      

        nova_conta = [self.nome, self.cpf, self.idade, num_conta]
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='a', newline="") as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(nova_conta)

    def acessar_conta():
        conta = int(input("Digite o número da sua conta:\n-> "))
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                print(linha[3])
                print()
                if int(linha[3]) == conta:
                    print(f"Olá {linha[0]}\ncpf: {linha[1]}\nidade: {linha[2]}")
                    return
            print("Conta não existente")
                        
                      
                                      

# def salvar_conta():
