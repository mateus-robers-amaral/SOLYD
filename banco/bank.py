''' Crie um software de gerenciamento bancário.
Este poderá ser capaz de criar clientes e contas
cada cliente possui nome, cpf e idade
e cada conta possui um client, um saldo, limite, sacar, depositar e consultar saldo'''
import csv


class Cliente():
    def __init__(self, nome, cpf, idade, saldo):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo

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
        saldo = 0

        return [nome.title(), cpf, idade, saldo]

    def criar_conta(self):

        num_conta = 1000000
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                num_conta += 1
        print(
            f"O número da sua conta é {num_conta}.\nSeu saldo inicial é R$ {self.saldo}.")

        nova_conta = [self.nome, self.cpf, self.idade, num_conta, self.saldo]
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='a', newline="") as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(nova_conta)

    def acessar_conta():
        conta = int(input("Digite o número da sua conta:\n-> "))
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                if int(linha[3]) == conta:
                    print(
                        f"Olá {linha[0]}\nCPF: {linha[1]}\nidade: {linha[2]} anos\nSaldo: {linha[4]}")
                    print("Deseja realizar alguma operação?\n[1] Sim\n[2] Não")
                    opcao = int(input("-> "))
                    if opcao == 1:
                        print(
                            "Qual operação deseja realizar?\n[1] Sacar\n[2] Depositar\n[3] Transferir")
                        operacao = int(input("-> "))
                        if operacao == 1:
                            sacar = int(input("Quanto deseja sacar?\n-> "))
                            Cliente.saque(sacar, conta)
                        elif operacao == 2:
                            deposito = int(
                                input("Quanto deseja depositar?\n-> "))
                            Cliente.depositar(deposito, conta)
                        elif operacao == 3:
                            transferencia = int(input("Quanto deseja transferir?\n-> "))
                            conta_destino = int(
                                input("Para qual conta deseja enviar?\n-> "))
                            Cliente.transferir(Cliente, transferencia, conta, conta_destino)
                        else:
                            print("Escolha uma opção válida.")

                    return
            print("Conta não existente")

    def saque(sacar, conta):
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='r') as arquivo_leitura:
            leitor_csv = csv.reader(arquivo_leitura)
            linhas = list(leitor_csv)
            for linha in linhas:
                if int(linha[3]) == int(conta):
                    saldo = int(linha[4])
                    if saldo >= sacar:
                        saldo -= sacar
                        linha[4] = saldo
                        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='w', newline='') as arquivo_escrita:
                            escritor_csv = csv.writer(arquivo_escrita)
                            escritor_csv.writerows(linhas)
                            print(
                                f"Operação efetuada com sucesso!\nNovo saldo: {saldo}")
                            return saldo
                    else:
                        print("Saldo insuficiente.")
                        return
            print("Conta não encontrada.")
            return

    def depositar(deposito, conta):
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='r') as arquivo_leitura:
            leitor_csv = csv.reader(arquivo_leitura)
            linhas = list(leitor_csv)
            for linha in linhas:
                if int(linha[3]) == int(conta):
                    saldo = int(linha[4])
                    saldo += deposito
                    linha[4] = str(saldo)
                    break
        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='w', newline='') as arquivo_escrita:
            escritor_csv = csv.writer(arquivo_escrita)
            escritor_csv.writerows(linhas)

    def transferir(self, transferencia, conta, conta_destino):
        self.saque(transferencia, conta)
        self.depositar(transferencia, conta_destino)
